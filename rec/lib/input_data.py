import pandas as pd


class input_data:
    """
    Class for modification of the input data for processing into main function
    """
    # pylint: disable=R0903
    # pylint: disable=E0602
    # pylint: disable=C0114
    # pylint: disable=C0305
    # pylint: disable=W0612
    def __init__(self):
        self.input_path = "./data/input/"
        self.catalog_file = self.input_path + "catalog.csv"
        self.user_preferences = self.input_path + "users.csv"
        self.catalog_data = pd.read_csv(self.catalog_file)
        self.users_preference_data = pd.read_csv(self.user_preferences)

    def return_files(self):
        """
        high level support for doing this and that.
        """
        return self.catalog_data, self.users_preference_data

    def pre_process_data(self):
        """
        high level support for doing this and that.
        """
        list_catalog = []
        for index, row in self.catalog_data.iterrows():
            in_dict = dict()
            list_prefs = []
            site = row["site"]
            rest_a = row["a1"]
            rest_b = row["a2"]
            rest_c = row["a3"]
            rest_d = row["a4"]
            rest_e = row["a5"]
            list_prefs.append(rest_a)
            list_prefs.append(rest_b)
            list_prefs.append(rest_c)
            list_prefs.append(rest_d)
            list_prefs.append(rest_e)
            in_dict[site] = list_prefs
            list_catalog.append(in_dict)

        list_users = []
        for index, row in self.users_preference_data.iterrows():
            in_dict = dict()
            list_prefs = []
            guest = row["guest"]
            rest_a = row["a1"]
            rest_b = row["a2"]
            rest_c = row["a3"]
            rest_d = row["a4"]
            rest_e = row["a5"]
            list_prefs.append(rest_a)
            list_prefs.append(rest_b)
            list_prefs.append(rest_c)
            list_prefs.append(rest_d)
            list_prefs.append(rest_e)
            in_dict[guest] = list_prefs
            list_users.append(in_dict)
        return list_catalog, list_users
