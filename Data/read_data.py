import pandas as pd


class Data:

    def __init__(self, data_path):

        self.path = data_path

    def get_data(self):

        return pd.read_csv(self.path)