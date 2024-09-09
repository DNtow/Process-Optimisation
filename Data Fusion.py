# data_fusion.py
import pandas as pd

def integrate_data(data_sources):
    df_list = [pd.read_csv(src) for src in data_sources]
    combined_df = pd.concat(df_list, axis=0)
    combined_df.fillna(method='ffill', inplace=True)
    return combined_df
