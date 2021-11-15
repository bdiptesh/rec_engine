import pandas as pd


class input_data:
    def __init__(self):
        self.input_path = "./data/input/"
        self.catalog_file = self.input_path + "catalog.csv"
        self.user_preferences = self.input_path + "users.csv"
        self.catalog_data = pd.read_csv(self.catalog_file)
        self.users_preference_data = pd.read_csv(self.user_preferences)

    def return_files(self):
        return self.catalog_data, self.users_preference_data

    def pre_process_data(self):
        list_catalog = []
        for index, row in self.catalog_data.iterrows():
            in_dict = dict()
            list_prefs = []
            site = row["site"]
            a = row["a1"]
            b = row["a2"]
            c = row["a3"]
            d = row["a4"]
            e = row["a5"]
            list_prefs.append(a)
            list_prefs.append(b)
            list_prefs.append(c)
            list_prefs.append(d)
            list_prefs.append(e)
            in_dict[site] = list_prefs
            list_catalog.append(in_dict)

        list_users = []
        for index, row in self.users_preference_data.iterrows():
            in_dict = dict()
            list_prefs = []
            guest = row["guest"]
            a = row["a1"]
            b = row["a2"]
            c = row["a3"]
            d = row["a4"]
            e = row["a5"]
            list_prefs.append(a)
            list_prefs.append(b)
            list_prefs.append(c)
            list_prefs.append(d)
            list_prefs.append(e)
            in_dict[guest] = list_prefs
            list_users.append(in_dict)
        return list_catalog, list_users
