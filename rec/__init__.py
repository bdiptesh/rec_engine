#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 06:39:44 2021

@author: ravi.kolluri
"""

# pylint: disable=invalid-name
# pylint: disable=wrong-import-position

import re
import sys

from inspect import getsourcefile
from os.path import abspath

# Set base path
path = abspath(getsourcefile(lambda: 0))
path = re.sub(r"(.+)(\/mllib.*)", "\\1", path)

sys.path.insert(0, path)