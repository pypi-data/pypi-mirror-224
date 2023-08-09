"""Run GENERIC TECHs LVS.

Usage:
    run_lvs.py (--help| -h)
    run_lvs.py (--layout=<layout_path>) (--netlist=<netlist_path>) [--thr=<thr>] [--run_dir=<run_dir_path>] [--topcell=<topcell_name>] [--run_mode=<run_mode>] [--verbose] [--lvs_sub=<sub_name>] [--no_net_names] [--spice_comments] [--scale]

Options:
    --help -h                           Print this help message.
    --layout=<layout_path>              The input GDS file path.
    --netlist=<netlist_path>            The input netlist file path.
    --thr=<thr>                         The number of threads used in run.
    --run_dir=<run_dir_path>            Run directory to save all the results [default: pwd]
    --topcell=<topcell_name>            Topcell name to use.
    --run_mode=<run_mode>               Select klayout mode Allowed modes (flat , deep, tiling). [default: deep ]
    --lvs_sub=<sub_name>                Substrate name used in your design.
    --verbose                           Detailed rule execution log for debugging.
    --no_net_names                      Discard net names in extracted netlist.
    --spice_comments                    Enable netlist comments in extracted netlist.
    --scale                             Enable scale of 1e6 in extracted netlist.
"""

import logging
import os
from datetime import datetime
from subprocess import check_call

import klayout.db
from docopt import docopt


def check_klayout_version() -> None:
    """
    check_klayout_version checks klayout version and makes sure it would work with the LVS.
    """
    # ======= Checking Klayout version =======
    klayout_v_ = os.popen("klayout -b -v").read()
    klayout_v_ = klayout_v_.split("\n")[0]
    klayout_v_list = []

    if klayout_v_ == "":
        logging.error("Klayout is not found. Please make sure klayout is installed.")
        exit(1)
    else:
        klayout_v_list = [int(v) for v in klayout_v_.split(" ")[-1].split(".")]

    if len(klayout_v_list) < 1 or len(klayout_v_list) > 3:
        logging.error("Was not able to get klayout version properly.")
        exit(1)
    elif len(klayout_v_list) >= 2 or len(klayout_v_list) <= 3:
        if klayout_v_list[1] < 28:
            logging.error("Prerequisites at a minimum: KLayout 0.28.0")
            logging.error(
                "Using this klayout version has not been assesed in this development. Limits are unknown"
            )
            exit(1)

    logging.info(f"Your Klayout version is: {klayout_v_}")


def check_layout_type(layout_path):
    """
    check_layout_type checks if the layout provided is GDS or OAS. Otherwise, kill the process. We only support GDS or OAS now.

    Parameters
    ----------
    layout_path : string
        string that represent the path of the layout.

    Returns
    -------
    string
        string that represent full absolute layout path.
    """

    if not os.path.isfile(layout_path):
        logging.error(
            f"## GDS file path {layout_path} provided doesn't exist or not a file."
        )
        exit(1)

    if ".gds" not in layout_path and ".oas" not in layout_path:
        logging.error(
            f"## Layout {layout_path} is not in GDSII or OASIS format. Please use gds format."
        )
        exit(1)

    return os.path.abspath(layout_path)


def get_top_cell_names(gds_path):
    """
    get_top_cell_names get the top cell names from the GDS file.

    Parameters
    ----------
    gds_path : string
        Path to the target GDS file.

    Returns
    -------
    List of string
        Names of the top cell in the layout.
    """
    layout = klayout.db.Layout()
    layout.read(gds_path)
    top_cells = [t.name for t in layout.top_cells()]

    return top_cells


def get_run_top_cell_name(arguments, layout_path):
    """
    get_run_top_cell_name Get the top cell name to use for running. If it's provided by the user, we use the user input.
    If not, we get it from the GDS file.

    Parameters
    ----------
    arguments : dict
        Dictionary that holds the user inputs for the script generated by docopt.
    layout_path : string
        Path to the target layout.

    Returns
    -------
    string
        Name of the topcell to use in run.

    """

    if arguments["--topcell"]:
        topcell = arguments["--topcell"]
    else:
        layout_topcells = get_top_cell_names(layout_path)
        if len(layout_topcells) > 1:
            logging.error(
                "## Layout has multiple topcells. Please use --topcell to determine which topcell you want to run on."
            )
            exit(1)
        else:
            topcell = layout_topcells[0]

    return topcell


def generate_klayout_switches(arguments, layout_path, netlist_path):
    """
    parse_switches Function that parse all the args from input to prepare switches for LVS run.

    Parameters
    ----------
    arguments : dict
        Dictionary that holds the arguments used by user in the run command. This is generated by docopt library.
    layout_path : string
        Path to the layout file that we will run LVS on.
    netlist_path : string
        Path to the netlist file that we will run LVS on.

    Returns
    -------
    dict
        Dictionary that represent all run switches passed to klayout.
    """
    switches = dict()

    # No. of threads
    thrCount = 2 if arguments["--thr"] is None else int(arguments["--thr"])
    switches["thr"] = str(int(thrCount))

    if arguments["--run_mode"] in ["flat", "deep", "tiling"]:
        switches["run_mode"] = arguments["--run_mode"]
    else:
        logging.error("Allowed klayout modes are (flat , deep , tiling) only")
        exit()

    if arguments["--lvs_sub"]:
        switches["lvs_sub"] = arguments["--lvs_sub"]
    else:
        switches["lvs_sub"] = "generic_tech_gnd"

    if arguments["--verbose"]:
        switches["verbose"] = "true"
    else:
        switches["verbose"] = "false"

    if arguments["--no_net_names"]:
        switches["spice_net_names"] = "false"
    else:
        switches["spice_net_names"] = "true"

    if arguments["--spice_comments"]:
        switches["spice_comments"] = "true"
    else:
        switches["spice_comments"] = "false"

    if arguments["--scale"]:
        switches["scale"] = "true"
    else:
        switches["scale"] = "false"

    switches["topcell"] = get_run_top_cell_name(arguments, layout_path)
    switches["input"] = os.path.abspath(layout_path)
    switches["schematic"] = os.path.abspath(netlist_path)

    return switches


def build_switches_string(sws: dict):
    """
    build_switches_string Build switches string from dictionary.

    Parameters
    ----------
    sws : dict
        Dictionary that holds the Antenna switches.
    """
    return " ".join(f"-rd {k}={v}" for k, v in sws.items())


def check_lvs_results(results_db_files: list) -> None:
    """
    check_lvs_results Checks the results db generated from run and report at the end if the LVS run failed or passed.

    Parameters
    ----------
    results_db_files : list
        A list of strings that represent paths to results databases of all the LVS runs.
    """

    if len(results_db_files) < 1:
        logging.error("Klayout did not generate any db results. Please check run logs")
        exit(1)


def run_check(lvs_file: str, path: str, run_dir: str, sws: dict):
    """
    run_check run LVS check.

    Parameters
    ----------
    lvs_file : str
        String that has the file full path to run.
    path : str
        String that holds the full path of the layout.
    run_dir : str
        String that holds the full path of the run location.
    sws : dict
        Dictionary that holds all switches that needs to be passed to the antenna checks.

    Returns
    -------
    string
        string that represent the path to the results output database for this run.

    """

    logging.info(
        f'Running GENERIC TECH {lvs_file} checks on design {path} on cell {sws["topcell"]}'
    )

    layout_base_name = os.path.basename(path).split(".")[0]
    new_sws = sws.copy()
    report_path = os.path.join(run_dir, f"{layout_base_name}.lvsdb")
    ext_net_path = os.path.join(run_dir, f"{layout_base_name}.cir")
    new_sws["report"] = report_path
    new_sws["target_netlist"] = ext_net_path

    sws_str = build_switches_string(new_sws)

    run_str = f"klayout -b -r {lvs_file} {sws_str}"
    check_call(run_str, shell=True)

    return report_path


def main(lvs_run_dir: str, arguments: dict) -> None:
    """
    main function to run the LVS.

    Parameters
    ----------
    lvs_run_dir : str
        String with absolute path of the full run dir.
    arguments : dict
        Dictionary that holds the arguments used by user in the run command. This is generated by docopt library.
    """

    ## Check Klayout version
    check_klayout_version()

    ## Check layout file existence
    layout_path = arguments["--layout"]
    if not os.path.exists(arguments["--layout"]):
        logging.error(
            f"The input GDS file path {layout_path} doesn't exist, please recheck."
        )
        exit(1)

    ## Check layout type
    layout_path = check_layout_type(layout_path)

    # Check netlist file existence
    netlist_path = arguments["--netlist"]
    if not os.path.exists(arguments["--netlist"]):
        logging.error(
            f"The input netlist file path {netlist_path} doesn't exist, please recheck."
        )
        exit(1)

    lvs_rule_deck = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "generic_tech.lvs"
    )

    ## Get run switches
    switches = generate_klayout_switches(arguments, layout_path, netlist_path)

    ## Run LVS check
    res_db_files = run_check(lvs_rule_deck, layout_path, lvs_run_dir, switches)

    ## Check run
    check_lvs_results(res_db_files)


if __name__ == "__main__":
    # arguments
    arguments = docopt(__doc__, version="RUN LVS: 1.0")

    # logs format
    now_str = datetime.utcnow().strftime("lvs_run_%Y_%m_%d_%H_%M_%S")

    if (
        arguments["--run_dir"] == "pwd"
        or arguments["--run_dir"] == ""
        or arguments["--run_dir"] is None
    ):
        lvs_run_dir = os.path.join(os.path.abspath(os.getcwd()), now_str)
    else:
        lvs_run_dir = os.path.abspath(arguments["--run_dir"])

    os.makedirs(lvs_run_dir, exist_ok=True)

    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler(os.path.join(lvs_run_dir, f"{now_str}.log")),
            logging.StreamHandler(),
        ],
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%d-%b-%Y %H:%M:%S",
    )

    # Calling main function
    main(lvs_run_dir, arguments)
