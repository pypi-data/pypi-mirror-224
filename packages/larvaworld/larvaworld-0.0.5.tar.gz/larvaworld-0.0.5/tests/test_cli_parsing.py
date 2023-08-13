# test_mock_argparse.py
import argparse
import os
SCRIPTS_DIR =os.path.dirname(os.path.abspath(__file__))
from larvaworld.lib import reg
print(reg.CONFTYPES)

try:
    from unittest import mock  # python 3.3+
except ImportError:
    import mock  # python 2.6-3.2
SCRIPTS_DIR =os.path.dirname(os.path.abspath(__file__))
# import larvaworld
from larvaworld.lib import reg, aux, sim

from larvaworld.cli.argparser import SimModeParser


def main():

    MP=SimModeParser()

    args = MP.cli_parser.parse_args()
    print(args)  # NOTE: this is how you would check what the kwargs are if you're unsure
    MP.args = aux.AttrDict(vars(args))
    MP.configure(show_args=True)

    return MP.args


@mock.patch('argparse.ArgumentParser.parse_args',
            return_value=argparse.Namespace(sim_mode='Exp', id=None))
def test_command(mock_args):
    res = main()
    # assert res == 6, "1 + 2 + 3 = 6"


if __name__ == "__main__":
    print(main())