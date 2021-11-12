from typing import List, Dict

import pandas as pd


class _Recommendation():

    """Short summary.

    Parameters
    ----------
    df_catalog : pd.DataFrame
        Catalog contains the site of the restaurants with the ref


    df_uid : pd.DataFrame
        Description of parameter `df_uid`.
    k : int
        Description of parameter `k` (the default is 3).

    Returns
    -------
    type
        Returns the sites with the scores of the recommended restaurants

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
        self.dict_uid: Dict[int, List[int]] = None
        self.df_uid: Dict[int, List[int]] = dict()
        for i in range(len(self.df_uid)):
            self.df_uid[df_uid.iloc[i,0]] = list(self.df_uid.iloc[i, 1:6])
        self.op = dict()

    def rec(self):
        """Short summary.

        Returns
        -------
        type
            Returning the output of recommended restaurants for the users.

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
        # Loop through users here
        self.op = dict()
        for i in self.df_uid:
            if df_uid[i].count(1) == 0:
                self.op[i] = []
            else: 
                self.op[i] = _top_rec(df_uid[i])
        return self.op


class RecommendationMatch(_Recommendation):
    def _top_rec(self,
                 user: List[int]):
       	"""Short summary.

        Returns
        -------
        type
            Returning a list of sorted items according to the scores. 
            

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
        score = {}
        for j in self.list_catalog:
            score[j] = np.count_nonzero((np.array(user) & np.array(list_catalog[j]))==1)/list_catalog[j].count(1)
        sort_score = dict(sorted(score.items(), key=lambda x: x[1], reverse=True))
        return (list(sort_score.items())[:self.k])


# =============================================================================
# --- Main
# =============================================================================

df_catalog = pd.read_csv('/home/manavi/rec_engine-feature_01/data/input/catalog.csv')
df_uid = pd.read_csv('/home/manavi/rec_engine-feature_01/data/input/users.csv')

rec_obj = RecommendationMatch(df_catalog, df_uid,1)
rec_op = rec_obj.rec()
