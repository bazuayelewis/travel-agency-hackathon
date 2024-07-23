import pandas as pd

def read_data(data_path: str):
    data_df = pd.read_csv(data_path)

    return data_df