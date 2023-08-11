import json
import logging
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

import numpy as np
import pkg_resources
import typer
from module_qc_data_tools import (
    get_env,
    get_layer_from_sn,
    get_sn_from_connectivity,
    outputDataFrame,
    qcDataFrame,
    save_dict_list,
)
from tabulate import tabulate

from module_qc_tools.cli.globals import (
    CONTEXT_SETTINGS,
    OPTIONS,
    LogLevel,
)
from module_qc_tools.utils.misc import (
    bcolors,
    check_meas_config,
)
from module_qc_tools.utils.ntc import ntc
from module_qc_tools.utils.power_supply import power_supply
from module_qc_tools.utils.yarr import yarr

if sys.version_info >= (3, 9):
    from importlib import resources
else:
    import importlib_resources as resources

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("measurement")

app = typer.Typer(context_settings=CONTEXT_SETTINGS)


def run(data, IV_config, ps, hv, nt, layer):
    # get current status
    lv_status = {"voltage": ps.getV(), "current": ps.getI()}
    log.debug("lv_status " + str(lv_status))
    hv_status = {"voltage": hv.getV(), "current": hv.getI()}
    log.debug("hv_status " + str(hv_status))

    # turn off LV and HV, set HV for measurement
    if (
        hv_status["voltage"][0] and hv_status["current"][0]
    ):  # if both HV voltage and current are != 0 then HV is on
        log.debug(
            "HV voltage: "
            + str(hv_status["voltage"][0])
            + " HV current: "
            + str(hv_status["current"][0])
        )
        log.info("Ramping HV to 0V before starting measurement...")
        hv.rampV(v=0, i=IV_config["i_max"][layer])
        hv.off()

    if (
        lv_status["voltage"][0] and lv_status["current"][0]
    ):  # if both LV voltage and current are != 0 then LV is on
        log.debug(
            "LV voltage: "
            + str(lv_status["voltage"][0])
            + " LV current: "
            + str(lv_status["current"][0])
        )
        log.info("Switching off LV before starting measurement...")
        ps.off()

    hv.set(v=IV_config["v_min"][layer], i=IV_config["i_max"][layer])
    if "emulator" not in hv.on_cmd:
        hv.on()

    voltages = np.linspace(
        IV_config["v_min"][layer],
        IV_config["v_max"][layer],
        IV_config["n_points"][layer],
    )
    starttime = time.time()
    log.info(
        "--------------------------------------------------------------------------"
    )
    for value in voltages:
        mea = {}
        # set and measure current for power supply
        hv.set(v=value, i=IV_config["i_max"][layer])  # has already a pause of 1 sec
        # time.sleep(1) ## 4 seconds between each step with this

        duration = time.time() - starttime
        voltage, v_status = hv.getV()
        currents = []
        for _j in range(3):  ## takes 0.5s for 3 readings
            duration = time.time() - starttime
            current, i_status = hv.getI()
            currents.append(current)
            log.debug(str(duration) + " " + str(current))
        temp, temp_status = nt.read()
        # TODO: humidity: interface with influxDB?

        mea["time"] = [duration]
        mea["voltage"] = [voltage]
        mea["current"] = [np.mean(currents)]
        mea["sigma current"] = [np.std(currents)]
        mea["temperature"] = [temp]
        data.add_data(mea)
        log.info(tabulate(mea, headers="keys"))

    time.sleep(1)
    # Return to initial state
    log.info(f'Ramping HV back to initial state at {hv_status["voltage"][0]}V...')
    hv.rampV(v=hv_status["voltage"][0], i=hv_status["current"][0])
    ps.set(v=lv_status["voltage"][0], i=lv_status["current"][0])
    if "emulator" not in ps.on_cmd:
        ps.on()


@app.command()
def main(
    config_path: Path = OPTIONS["config"],
    base_output_dir: Path = OPTIONS["output_dir"],
    module_connectivity: Optional[Path] = OPTIONS["module_connectivity"],
    verbosity: LogLevel = OPTIONS["verbosity"],
    use_pixel_config: bool = OPTIONS["use_pixel_config"],
    site: str = OPTIONS["site"],
    vdepl: float = OPTIONS["depl_volt"],
):
    log.setLevel(verbosity.value)

    log.info("[run_IV_MEASURE] Start IV scan!")
    timestart = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    log.info(f"[run_IV_MEASURE] TimeStart: {timestart}")

    with resources.as_file(Path(config_path)) as path:
        config = json.loads(path.read_text())

    check_meas_config(config, config_path)

    # Need to pass module connectivity path to yarr class (except in case we are running the emulator)
    if module_connectivity:
        config["yarr"]["connectivity"] = module_connectivity

    # connectivity for emulator is defined in config, not true when running on module (on purpose)
    if "emulator" not in str(config_path) and not module_connectivity:
        typer.echo("must supply path to connectivity file [-m --module-connectivity]")
        raise typer.Exit(2)

    IV_config = config["tasks"]["GENERAL"]
    IV_config.update(config["tasks"]["IV_MEASURE"])
    ps = power_supply(config["power_supply"])
    hv = power_supply(config["high_voltage"], name="high_voltage")
    nt = ntc(config["ntc"])
    yr = yarr(config["yarr"])

    # Define identifires for the output files.
    # Taking the module SN from YARR path to config in the connectivity file.
    # Taking the test-type from the script name which is the test-code in ProdDB.
    module_serial = get_sn_from_connectivity(config["yarr"]["connectivity"])
    layer = get_layer_from_sn(module_serial)
    test_type = Path(__file__).stem
    institution = get_env("INSTITUTION")
    if site and institution is not None:
        log.warning(
            bcolors.WARNING
            + " Overwriting default institution {} with manual input {}!".format(
                institution, site
            )
            + bcolors.ENDC
        )
        institution = site
    elif site:
        institution = site

    if not institution:
        log.error(
            bcolors.ERROR
            + 'No institution found. Please specify your testing site as an environmental variable "INSTITUTION" or specify with the --site option. '
            + bcolors.ENDC
        )
        return

    # if -o option used, overwrite the default output directory
    output_dir = module_connectivity.parent if module_connectivity else base_output_dir

    if base_output_dir != Path("outputs"):
        output_dir = base_output_dir

    output_dir = output_dir.joinpath("Measurements", test_type, timestart)
    # Make output directory and start log file
    output_dir.mkdir(parents=True, exist_ok=True)
    log.addHandler(logging.FileHandler(output_dir.joinpath("output.log")))

    data = qcDataFrame(
        columns=[
            "time",
            "voltage",
            "current",
            "sigma current",
            "temperature",
            "humidity",
        ],
        units=["s", "V", "A", "A", "C", "%"],
    )

    data.set_x("voltage", True)
    data.add_meta_data("Institution", institution)
    data.add_meta_data("ModuleSN", module_serial)
    data.add_meta_data("TimeStart", round(datetime.timestamp(datetime.now())))
    data.add_property(
        test_type + "_MEASUREMENT_VERSION",
        pkg_resources.get_distribution("module-qc-tools").version,
    )

    try:
        run(data, IV_config, ps, hv, nt, layer)
    except KeyboardInterrupt:
        log.info("KeyboardInterrupt")
    except Exception as err:
        log.exception(err)
        raise typer.Exit(1) from err

    data.add_meta_data("TimeEnd", round(datetime.timestamp(datetime.now())))
    data.add_meta_data("DepletionVoltage", vdepl)
    data.add_meta_data("AverageTemperature", np.average(data["temperature"]))

    # save results in json
    log.info(
        "==================================Summary=================================="
    )
    alloutput = []
    log.info(data)
    outputDF = outputDataFrame()
    outputDF.set_test_type(test_type)
    outputDF.set_results(data)
    alloutput += [outputDF.to_dict()]
    save_dict_list(
        output_dir.joinpath(f"{module_serial}.json"),
        alloutput,
    )

    log.info(f"Writing output measurements in {output_dir}")
    log.info("[run_IV-MEASURE] Done!")
    timeend = datetime.now()
    duration = timeend - datetime.strptime(timestart, "%Y-%m-%d_%H%M%S")

    log.info(f"[run_IV-MEASURE] TimeEnd: {timeend.strftime('%Y-%m-%d_%H%M%S')}")
    log.info(f"[run_IV-MEASURE] Duration: {duration}")

    # Delete temporary files
    if not use_pixel_config:
        yr.remove_tmp_connectivity()


if __name__ == "__main__":
    typer.run(main)
