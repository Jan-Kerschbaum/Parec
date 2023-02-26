import pandas as pd

def load_data_dummy():
    data = pd.read_csv(r"./app/data/reduced_data.csv")
    data = data.dropna()
    return data