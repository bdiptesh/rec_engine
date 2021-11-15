
import pandas as pd
from scipy import spatial

class Recommendation():
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

    def __init__(self,
                 k : int = 3):
        self.k = k
        self.inp_data = input_data()
        self.list_catalog_data, self.list_user_preferences = self.inp_data.pre_process_data()
        self.df_catalog, self.df_uid = self.inp_data.return_files()
        self.op = None


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
        self.op = []
        for each_user in self.list_user_preferences:
            user_id = list(each_user.keys())[0]
            prefs = each_user[user_id]
            for each_restaurant in self.list_catalog_data:
                rest_id = list(each_restaurant.keys())[0]
                rest_catalog = each_restaurant[rest_id]
                similarity =  - spatial.distance.cosine(prefs, rest_catalog)
                in_dict = dict()
                in_dict["user_id"] = user_id
                in_dict["restaurant_id"] = rest_id
                in_dict["match_score"] = similarity
                self.op.append(in_dict)
        distance_matrix = pd.DataFrame(self.op)
        distance_matrix["rank"] = distance_matrix.groupby("user_id")["match_score"].rank("dense", ascending=False)
        distance_matrix = distance_matrix[(distance_matrix["rank"] <= self.k)]
        return distance_matrix


# =============================================================================
# --- Main
# =============================================================================

recommendations = Recommendation(5)
recommed = recommendations.rec()

"""
# rec_obj = RecommendationSimpleMatch(df_catalog, df_uid)
rec_obj = RecommendationComplexMatch(df_catalog, df_uid, k=10)
rec_op = rec_obj.rec()
"""

