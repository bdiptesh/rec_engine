"""
Main File

Credits
-------
::

    Authors:
        - Manavi

    Date: Nov 8, 2021
"""

from lib.rec_engine import Recommendation, pd

DFCATALOG = pd.read_csv('../data/input/catalog.csv')
DFUSER = pd.read_csv('../data/input/users.csv')

OBJ = Recommendation(DFCATALOG, DFUSER, 3)
REC_OP = OBJ.rec()

print(REC_OP)
