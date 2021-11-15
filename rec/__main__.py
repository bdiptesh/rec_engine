"""
Recommendation engine.

Objective:
    - Illustrate module APIs with some examples.

Credits
-------
::

    Authors:
        - Diptesh

    Date: Oct 30, 2021
"""

# pylint: disable=invalid-name

# =============================================================================
# --- Import libraries
# =============================================================================

import argparse
import time

import pandas as pd

from lib import cfg, utils  # noqa: F841
from lib.rec_engine import RecommendationMatch  # noqa: F841

# =============================================================================
# --- DO NOT CHANGE ANYTHING FROM HERE
# =============================================================================

__version__ = cfg.__version__
__doc__ = cfg.__doc__
path = cfg.path + "data/"
elapsed_time = utils.elapsed_time

sep = "-" * 70
print(sep, "\n" + __doc__, "v" + __version__, "\n" + sep + "\n")

# =============================================================================
# --- Arguments
#
# catalog: str
# users: str
# =============================================================================

CLI = argparse.ArgumentParser()

CLI.add_argument("-c", "--catalog",
                 nargs=1,
                 type=str,
                 default=["catalog.csv"],
                 help="catalog csv filename")

CLI.add_argument("-u", "--users",
                 nargs=1,
                 type=str,
                 default=["users.csv"],
                 help="user preferences csv filename")

args = CLI.parse_args()

fn_cat = args.catalog[0]
fn_uid = args.users[0]

# =============================================================================
# --- Main
# =============================================================================

if __name__ == '__main__':
    start = time.time_ns()
    # Load the data
    df_cat = pd.read_csv(path + "input/" + fn_cat)
    df_uid = pd.read_csv(path + "input/" + fn_uid)
    # Find recommendations
    rec_obj = RecommendationMatch(catalog=df_cat, user_preference=df_uid, k=3)
    rec_op = rec_obj.rec()
    # Print/save output
    rec_op.to_csv(path + "output/rec_" + fn_uid, index=False)
    # # --- EOF
    print(sep, elapsed_time("Total time", start), sep, sep="\n")
