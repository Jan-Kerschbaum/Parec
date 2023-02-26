import pandas as pd

def load_data_dummy():
    data = pd.read_csv(r"./app/data/arxiv_reduced_modified.json")
    data = data.dropna()
    return data