# importing libraries

import pandas as pd
import numpy as np

# creating a dataframe with missing values in columns

df = pd.DataFrame({
                    "Column_1":[255, 128, 64, None, None],
                    "Column_2":[0, 25, None, 64, 177],
                    "Column_3":[77, None, None, 90, 120],
                    "Column_4":[55, None, 65, None, 99],
                    "Column_5":[None, 36, 67, 212, 252]
                })

# define various methods of imputing

def mean_imputer(df):
    df = df.convert_dtypes()
    column_names = df.columns.tolist()
    for i in column_names:
        df[i].fillna(int(df[i].mean()),inplace=True)
    return df

def median_imputer(df):
    df = df.convert_dtypes()
    column_names = df.columns.tolist()
    for i in column_names:
        df[i].fillna(int(df[i].median()),inplace=True)
    return df

def mode_imputer(df):
    df = df.convert_dtypes()
    column_names = df.columns.tolist()
    for i in column_names:
        df[i].fillna(int(max(df[i].mode())),inplace=True)
    return df

# linking the imputer function with method to be used

def imputer(df,method):
    if (method == "mean"):
        df = mean_imputer(df)
    elif (method == "median"):
         df = median_imputer(df)
    else:
        (method == "mode")
        df = mode_imputer(df)
    return df

# test

print(imputer(df,method="mean"))