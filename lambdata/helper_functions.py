"""Lambdata - a collection of helper functions"""

import pandas as pd
import numpy as np

def list_2_series(list_2_series, df):
    new_df=df.copy
    series = pd.series(list_2_series)
    new_df.append(series)

    return(new_df)

def rm_outlier(df):
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    iqr = q3-q1 #Interquartile range
    fence_low  = q1-1.5*iqr
    fence_high = q3+1.5*iqr
    return df_out

""" def null_count(df:pd.DataFrame) -> int:
    null_sum=0
    columns=df.isna().sum()
    for i in columns:
        null_sum += columns[i]

    return null_sum

def train_test_split(df:pd.DataFrame, train_size=float) -> (pd.DataFrame, pd.Dataframe):
    temp_df=df.copy()
    training = temp_df.sample(frac=train_size, random_state=42)
    testing=temp_df.drop(training.index).sample(frac=1, random_state=42)

    return training, testing """

