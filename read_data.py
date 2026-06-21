import pandas as pd

def load_data():
    df = pd.read_csv("personal_finance_dataset_8000_extended.csv")
    return df