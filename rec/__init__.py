"""
Initialization file for rec.

Credits
-------
::

    Authors:
        - Diptesh

    Date: Oct 30, 2021
"""

# pylint: disable=invalid-name
# pylint: disable=wrong-import-position

import re
import sys

from inspect import getsourcefile
from os.path import abspath

import pipreqs
import coverage

# Set base path
path = abspath(getsourcefile(lambda: 0))
path = re.sub(r"(.+)(\/rec.*)", "\\1", path)

sys.path.insert(0, path)

__all__ = ["pipreqs", "coverage", ]
