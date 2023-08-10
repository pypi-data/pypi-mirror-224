import sys
from cnextb.debug.terminal import main as terminal_main
from cnextb.device.scanDevices import *


def main(args):
    """
    Main function parses the arguments from the run command only

    """
    _parse_run_options(args)


def _parse_run_options(args):
    """
    Parses the command line argument supplied

    """

    found = False

    if len(args) > 0:
        run_options = _get_run_options()
        main_arg = args[0]
        for item in run_options:
            if item[0] == main_arg or item[1] == main_arg:
                found = True
                item[2](args[1:])

    if found is False:
        print("")
        print("ERROR - Command line argument not recognised")
        print("")
        _run_help_function()


def _get_run_options():
    """
    Gets the list of options for cnextb.run commands which can be called

    """
    run_options = list()

    run_options.append(["t", "terminal", _run_terminal_function, "Runs terminal script"])
    run_options.append(["h", "help", _run_help_function, "Displays help screen with a list of commands supported"])

    return run_options


def _run_terminal_function(args=None):
    """
    Runs terminal script

    """
    terminal_main()


def _run_help_function(args=None):
    """
    Shows help

    """
    print("cnextb.run - Available commands")
    run_options = _get_run_options()
    display_options = []
    for item in run_options:
        short_name = item[1]
        description = item[3]
        display_options.append([short_name, description])
    dispaly_table(display_options, align="l", table_headers=["Name", "Description"])


if __name__ == "__main__":
    main(sys.argv[1:])
