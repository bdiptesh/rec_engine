"""
Recommendation Engine File

Credits
-------
::

    Authors:
        - Manavi

    Date: Nov 8, 2021
"""


from typing import List, Dict

import pandas as pd
import numpy as np


class Recommendation():

    """Short summary.

    Parameters
    ----------
    df_catalog : pd.DataFrame
        Catalog contains the site of the restaurants with the preferences 
    df_uid : pd.DataFrame
        Contains the User ID along with the preferences in cuisine
    k : int
        The number of top recommendations that need to be given (the default is 3).

    Returns
    -------
    type
    	op: Dictionary
    		Output of User ID: int
    		List of Site and respective Score
        Returns the sites with the scores of the recommended restaurants

    """
    
    
    def __init__(self,
                 df_catalog: pd.DataFrame,
                 df_uid: pd.DataFrame,
                 k: int = 3):
        self.df_catalog = df_catalog
        self.df_uid = df_uid
        self.k = k
        self.list_catalog: Dict[int, List[int]] = dict()
        for i in range(len(self.df_catalog)):
            self.list_catalog[df_catalog.iloc[i,0]] = list(self.df_catalog.iloc[i, 1:6])
        self.dict_uid: Dict[int, List[int]] = dict()
        for i in range(len(self.df_uid)):
            self.dict_uid[df_uid.iloc[i,0]] = list(self.df_uid.iloc[i, 1:6])
        self.op = dict()
    
    def _top_rec(self,
                 user: List[int]):
       	"""Short summary.

        Returns
        -------
        type
            Returning a list of sorted items according to the scores. 

        """
        score = {}
        for j in self.list_catalog:
            score[j] = np.count_nonzero((np.array(user) & np.array(self.list_catalog[j]))==1)/user.count(1)
        sort_score = dict(sorted(score.items(), key=lambda x: x[1], reverse=True))
        return(list(sort_score.items())[:self.k])


    def rec(self):
        """Short summary.

        Returns
        -------
        type
            op: Dictionary
            Returning the output of recommended restaurants for the users.

        """
        # Loop through users here
        self.op = dict()
        for i in self.dict_uid:
            if self.dict_uid[i].count(1) == 0:
                self.op[i] = []
            else: 
                self.op[i] = self._top_rec(self.dict_uid[i])
        return self.op
  
# =============================================================================
# --- Main
# =============================================================================       
df_catalog = pd.read_csv('/home/manavi/rec_engine-feature_01/data/input/catalog.csv')
df_uid = pd.read_csv('/home/manavi/rec_engine-feature_01/data/input/users.csv')

rec_obj = Recommendation(df_catalog, df_uid,3)
rec_op = rec_obj.rec()
