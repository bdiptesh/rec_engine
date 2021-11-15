"""
Recommendation engine.

Objective:
    - Determine top ``k`` recommendations for each user.

Credits
-------
::

    Authors:
        - Diptesh

    Date: Oct 30, 2021
"""

# pylint: disable=invalid-name

from typing import List, Union

import pandas as pd

# =============================================================================
# --- DO NOT CHANGE ANYTHING FROM HERE
# =============================================================================


class _Recommendation():
    """Recommendation engine parent class.

    Parameters
    ----------
    catalog : pd.DataFrame

        Pandas dataframe containing site and assortments.

    user_preference : pd.DataFrame

        Pandas dataframe containing user preferences for each assortment. The
        assortment should be of the same length as of ``catalog``.

    k : int, optional

        Number of recommendations required for each user (the default is 3).

    Returns
    -------
    pd.DataFrame

        Recommendation output with the following columns::

            uid
            vendor
            match
            score

    Methods
    -------
    ``top_rec`` : This needs to be over-ridden in child classes.

    ``rec``

    """

    def __init__(self,
                 catalog: pd.DataFrame,
                 user_preference: pd.DataFrame,
                 k: int = 3):
        """Initialize variables for ``Recommendation``."""
        self.catalog = catalog
        self.user_preference = user_preference
        self.k = k
        self.dict_cat = catalog.set_index(catalog.columns[0]).T.to_dict('list')
        self.dict_user_pref = user_preference.set_index(user_preference.
                                                        columns[0]).T.\
            to_dict('list')
        self.rec_op = None

    def top_rec(self,
                user: List[int],
                uid: Union[int, str],
                k: int = 3
                ) -> List[List[Union[int, float]]]:  # pragma: no cover
        """Determine top ``k`` recommendations for the given user.

        Parameters
        ----------
        user : List[int]

            User preferences for each assortment.

        uid: Union[str, int]

            User identifier.

        k : int

            Number of recommendations required (the default is 3).

        Returns
        -------
        List[List[Union[int, float]]]

            Top ``k`` recommendations for the given user::

                [[uid, site, match, score], [uid, site, match, score], ...]
                where value is sorted from top 1 to top k.

        """
        dummy_op = [uid, -1, -1, -1.0 / sum(user)] * max(self.k, k)
        return dummy_op

    def rec(self) -> pd.DataFrame:
        """Determine recommendations.

        Returns
        -------
        pd.DataFrame

            Recommendation output with the following columns::

                uid
                vendor
                match
                score

        """
        rec_op = []
        for user in self.dict_user_pref.keys():
            tmp_op = self.top_rec(self.dict_user_pref[user],
                                  uid=user,
                                  k=self.k)
            rec_op.extend(tmp_op)
        self.rec_op = pd.DataFrame(data=rec_op,
                                   columns=[self.user_preference.columns[0],
                                            self.catalog.columns[0],
                                            "match", "score"])
        return self.rec_op


class RecommendationMatch(_Recommendation):
    """Recommendation engine.

    Parameters
    ----------
    catalog : pd.DataFrame

        Pandas dataframe containing site and assortments.

    user_preference : pd.DataFrame

        Pandas dataframe containing user preferences for each assortment. The
        assortment should be of the same length as of ``catalog``.

    k : int, optional

        Number of recommendations required for each user (the default is 3).

    Returns
    -------
    pd.DataFrame

        Recommendation output with the following columns::

            uid
            vendor
            match
            score

    Methods
    -------
    top_rec

    rec

    Examples
    --------
    >>> rec_obj = Recommendation(catalog=df_cat, user_preference=df_uid, k=5)
    >>> rec_op = rec_obj.rec()

    """

    def top_rec(self,
                user: List[int],
                uid: Union[int, str],
                k: int = 3) -> List[List[Union[int, float]]]:
        """Determine top ``k`` recommendations for the given user.

        Parameters
        ----------
        user : List[int]

            User preferences for each assortment.

        uid: Union[str, int]

            User identifier.

        k : int

            Number of recommendations required (the default is 3).

        Returns
        -------
        List[List[Union[int, float]]]

            Top ``k`` recommendations for the given user::

                [[uid, site, match, score], [uid, site, match, score], ...]
                where value is sorted from top 1 to top k.

        """
        assortment_len = len(user)
        tmp_op = []
        for vendor in self.dict_cat.keys():
            tmp_match = 0
            for assortment in range(assortment_len):
                if (self.dict_cat[vendor][assortment] == user[assortment])\
                   and (user[assortment] == 1):
                    tmp_match += 1
            tmp_op.append([uid, vendor, tmp_match, tmp_match/sum(user)])
        tmp_op = sorted(tmp_op, key=lambda x: x[3], reverse=True)[:k]
        return tmp_op
