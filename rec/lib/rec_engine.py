import operator
import os
from scipy import spatial

class Recommendation():
    # pylint: disable=R0903
    # pylint: disable=E0602
    # pylint: disable=C0114
    # pylint: disable=C0305
    """Short summary.

    Parameters
    ----------
    df_catalog : pd.DataFrame
        Description of parameter `df_catalog`.
    df_uid : pd.DataFrame
        Description of parameter `df_uid`.
    k : int
        Description of parameter `k` (the default is 3).

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

    def __init__(self, df_cat, df_user,
                 k:int = 3):
        

        self.df_catalog = df_cat
        self.df_uid = df_user
        self.k = k
        self.dict_catalog_pref = self.df_catalog.set_index(df_cat.columns[0])\
            .T.to_dict('list')
        self.dict_users_pref = self.df_uid.set_index(df_user.columns[0]).\
            T.to_dict('list')
        self.k = k
        self.op_var = None

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
        # Loop through usesr here
        self.op_var = {}
        for each_user, preference in self.dict_users_pref.items():
            user_id = each_user
            prefs = preference
            in_dict = dict()
            for each_restaurant, cuisine in self.dict_catalog_pref.items():
                rest_id = each_restaurant
                rest_catalog = cuisine
                similarity =  spatial.distance.cosine(prefs, rest_catalog)
                in_dict[rest_id] = similarity
            sorted_d = sorted(in_dict.items(), key=operator.itemgetter(1), reverse=True)
            self.op_var[user_id] = sorted_d[0:self.k]
        return self.op_var
