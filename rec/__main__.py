"""
Main File
Credits
-------
::
    Authors:
        - Deepak
    Date: Nov 15, 2021
"""

from lib.rec_engine import RecommendationFun, pd  # pylint: disable=E0401
df_catalog = pd.read_csv("../data/input/catalog.csv")
df_uid = pd.read_csv("../data/input/users.csv")
reco = RecommendationFun(df_catalog, df_uid, 3)
final_recommendation = reco.rec()
