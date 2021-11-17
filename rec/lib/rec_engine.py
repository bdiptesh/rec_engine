# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import pandas as pd
import numpy as np


class RecommendationFun():  # pylint: disable=R0903
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
    def __init__(self, df_cat, df_user, k: int = 3):
        self.df_catalog = df_cat
        self.df_uid = df_user
        self.k = k
        self.dict_catalog_pref = self.df_catalog.set_index(df_cat.columns[0])\
            .T.to_dict('list')
        self.dict_users_pref = self.df_uid.set_index(df_user.columns[0]).\
            T.to_dict('list')
        self.final1 = None
        self.final_list = None

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
        self.final1 = []
        for key1, values1 in self.dict_users_pref.items():
            user_id = key1
            prefs = values1
            for key, values in self.dict_catalog_pref.items():
                rest_id = key
                rest_catalog = values
                i = 0
                score = 0
                list1 = []
                for i in np.arange(0, len(prefs)):
                    if (prefs[i] == rest_catalog[i]) and (prefs[i] == 1):
                        score = score+1
                        score_perc = (score/sum(prefs))
                list1.append(user_id)
                list1.append(rest_id)
                list1.append(score)
                list1.append(score_perc)
                self.final1.append(list1)
        df_pre_final = pd.DataFrame(self.final1,
                                    columns=['User_id', 'Rest_id', 'Match',
                                             'Score'])
        df_final = df_pre_final.sort_values(
            ['User_id', 'Score'], ascending=[True, False]).\
            groupby('User_id').head(self.k)
        self.final_list = df_final.values.tolist()
        return self.final_list
