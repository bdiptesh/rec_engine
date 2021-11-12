import pandas as pd


class input_data:
    def __init__(self):
        self.input_path = "/home/ravi/rec_engine/data/input/"
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
            a1 = row["a1"]
            a2 = row["a2"]
            a3 = row["a3"]
            a4 = row["a4"]
            a5 = row["a5"]
            list_prefs.append(a1)
            list_prefs.append(a2)
            list_prefs.append(a3)
            list_prefs.append(a4)
            list_prefs.append(a5)
            in_dict[site] = list_prefs
            list_catalog.append(in_dict)

        list_users = []
        for index, row in self.users_preference_data.iterrows():
            in_dict = dict()
            list_prefs = []
            guest = row["guest"]
            a1 = row["a1"]
            a2 = row["a2"]
            a3 = row["a3"]
            a4 = row["a4"]
            a5 = row["a5"]
            list_prefs.append(a1)
            list_prefs.append(a2)
            list_prefs.append(a3)
            list_prefs.append(a4)
            list_prefs.append(a5)
            in_dict[guest] = list_prefs
            list_users.append(in_dict)
        return list_catalog, list_users
        pass
