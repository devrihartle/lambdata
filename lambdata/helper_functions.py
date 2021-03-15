"""Lambdata - a collection of helper functions"""

import pandas as pd
import numpy as np


class CountNulls:
    def __init__(df):
        self.DataFrame = df

    def null_count(self):
        null_sum=0
        columns=df.isna().sum()
        for i in columns:
            null_sum += columns[i]

        return null_sum

class SplitDates:
    def __init__(series)
        self.series = series

    def split_dates(self):
        self.month = self.series.dt.month
        self.day = self.series.dt.day
        self.year = self.series.dt.year
        self.frame = {"month": self.month, "day": self.day, "year": self.year}
        self.output = pd.DataFrame(self.frame)
        
        return self.output

