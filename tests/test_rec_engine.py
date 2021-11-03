"""
Test suite module for ``RecommendationMatch``.

Credits
-------
::

    Authors:
        - Diptesh

    Date: Oct 30, 2021
"""

# pylint: disable=invalid-name
# pylint: disable=wrong-import-position

import unittest
import warnings
import re
import sys

from inspect import getsourcefile
from os.path import abspath

import pandas as pd

# Set base path
path = abspath(getsourcefile(lambda: 0))
path = re.sub(r"(.+)(\/tests.*)", "\\1", path)

sys.path.insert(0, path)

from rec.lib.rec_engine import RecommendationMatch  # noqa: F841

# =============================================================================
# --- DO NOT CHANGE ANYTHING FROM HERE
# =============================================================================

path = path + "/data/input/"

# =============================================================================
# --- User defined functions
# =============================================================================


def ignore_warnings(test_func):
    """Suppress warnings."""

    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            test_func(self, *args, **kwargs)
    return do_test


class TestIntegrationRecommendationMatch(unittest.TestCase):
    """Test suite for module ``rec_engine``."""

    def setUp(self):
        """Set up for module ``rec_engine``."""

    def test_top_1(self):
        """Recommendation: Test for top 1."""
        df_cat = pd.DataFrame({"restaurant": [1, 2, 3, 4, 5],
                               "chinese": [1, 0, 1, 0, 1],
                               "indian": [0, 1, 0, 1, 0],
                               "sushi": [1, 1, 0, 1, 0]})
        df_uid = pd.DataFrame({"user": [1, 2],
                               "chinese": [1, 0],
                               "indian": [1, 1],
                               "sushi": [0, 0]})
        obj = RecommendationMatch(catalog=df_cat, user_preference=df_uid, k=1)
        op = obj.rec()
        exp_op = {1: [[0, 1, 0.5]], 2: [[1, 1, 1.0]]}
        self.assertEqual(op, exp_op)


# =============================================================================
# --- Main
# =============================================================================

if __name__ == '__main__':
    unittest.main()
