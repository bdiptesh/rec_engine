"""
Main File
Credits
-------
::
    Authors:
        - Deepak
    Date: Nov 15, 2021
"""

import time
from lib import utils # pylint: disable=E0401
from lib.rec_engine import RecommendationFun, pd # pylint: disable=E0401

SEP = '-' * 70
ELAPSED_TIME = utils.elapsed_time

START = time.time_ns()
df_catalog=pd.read_csv\
        ("../data/input/catalog.csv")
df_uid=pd.read_csv\
        ("../data/input/users.csv")
reco = RecommendationFun(df_catalog,df_uid,3)
final_recommendation = reco.rec()
print(SEP, ELAPSED_TIME("Total time", START), SEP, sep="\n")
