import pandas as pd

def load_data_dummy():
    data = pd.read_csv(r"./app/data/reduced_data_from_es.csv")
    data = data.dropna()
    return data