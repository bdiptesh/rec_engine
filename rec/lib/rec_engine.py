# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import pandas as pd
import numpy as np
class RecommendationFun(): # pylint: disable=R0903
    """Short summary.

    Parameters
    ----------
    df_catalog : pd.DataFrame
        This contains the features related to Restraunt`df_catalog`.
    df_uid : pd.DataFrame
        This contains the features related to User preferences `df_uid`.
    k : int
        How many recommendations do we want`k` (the default is 3).

    Returns
    -------
    type
        Description of returned object.
    Raises
    ------
    ExceptionName
        Why the exception is raised.
    Examples
    --------
    Examples should be written in doctest format, and
    should illustrate how to use the function/class.
    >>>
    """
    def __init__(self,k : int = 3):
        self.df_catalog = pd.read_csv\
        ("../../data/input/catalog.csvc")
        self.df_uid = pd.read_csv\
        ("../../data/input/users.csv")
        self.k = k
        self.dict_catalog_pref= self.df_catalog.iloc[0:6,:].set_index('site').T.to_dict('list')
        self.dict_users_pref= self.df_uid.iloc[0:6,:].set_index('guest').T.to_dict('list')
        self.final1=None
    def rec(self):
        """Short summary.
        Returns
        -------
        type
            Description of returned object.
        Raises
        ------
        ExceptionName
            Why the exception is raised.
        Examples
        --------
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>
        """
        self.final1=[]
        for key1, values1 in self.dict_users_pref.items():
            user_id = key1
            prefs = values1
            for key, values in self.dict_catalog_pref.items():
                rest_id = key
                rest_catalog = values
                i=0
                score=0
                list1=[]
                for i in np.arange(0, len(prefs)):
                    if (prefs[i]==rest_catalog[i]) and (prefs[i]==1):
                        score=score+1
                        score_perc=(score/sum(prefs))
                    else:
                        score_perc=0
                list1.append(user_id)
                list1.append(rest_id)
                list1.append(score_perc)
                self.final1.append(list1)
        df_pre_final=pd.DataFrame(self.final1,columns=['User_id','Rest_id','Score'])
        df_final=df_pre_final.sort_values\
        (['User_id','Score'],ascending=[True, False]).groupby('User_id').head(self.k)
        return df_final
# =============================================================================
# --- Main
# =============================================================================
reco = RecommendationFun(4)
final_recommendation = reco.rec()
