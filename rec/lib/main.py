"""
Main File

Credits
-------
::

    Authors:
        - Manavi

    Date: Nov 8, 2021
"""

from rec_engine import Recommendation, pd

DFCATALOG = pd.read_csv('/home/manavi/rec_engine-feature_01/data/input/catalog.csv')
DFUSER = pd.read_csv('/home/manavi/rec_engine-feature_01/data/input/users.csv')

OBJ = Recommendation(DFCATALOG, DFUSER, 3)
REC_OP = OBJ.rec()

print(REC_OP)
