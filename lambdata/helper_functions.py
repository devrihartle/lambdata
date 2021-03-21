"""Lambdata - a collection of helper functions"""

import pandas as pd
import numpy as np
import datetime


class CountNulls:
    def __init__(self, df):
        self.df = df

    def nullcount(self):
        return self.df.isnull().sum().sum()

class SplitDates:
    def __init__(self, series):
        self.series = series 

    def split_dates(self):
        if type(self.series) != pd.Series:
            self.series = pd.Series(self.series)
        if not isinstance(self.series.dtypes, datetime.datetime):
            self.series = pd.to_datetime(self.series)

        month = self.series.dt.month
        day = self.series.dt.day
        year = self.series.dt.year
        frame = {"month": month, "day": day, "year": year}
        df = pd.DataFrame(frame)
        
        return df

