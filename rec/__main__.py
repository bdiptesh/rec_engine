"""
Main File

Credits
-------
::

    Authors:
        - Manavi

    Date: Nov 8, 2021
"""

import time
from lib import utils
from lib.rec_engine import Recommendation, pd

SEP = '-' * 70
ELAPSED_TIME = utils.elapsed_time

START = time.time_ns()
DFCATALOG = pd.read_csv('../data/input/catalog.csv')
DFUSER = pd.read_csv('../data/input/users.csv')

OBJ = Recommendation(DFCATALOG, DFUSER, 3)
REC_OP = OBJ.rec()

print(REC_OP)
print(SEP, ELAPSED_TIME("Total time", START), SEP, sep="\n")
