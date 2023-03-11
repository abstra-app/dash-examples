import pandas as pd

# 1. This variable starts as None, see the widget binded to it
uploaded = None

# 2. This function gets a dataframe from this excel file
def get_dataframe():
    if (uploaded is None):
        return None
    return pd.read_excel(uploaded.file)