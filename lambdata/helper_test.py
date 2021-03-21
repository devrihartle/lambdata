"""a folder to test our helper functions and ensure they are working properly """

import pandas as pd
import numpy as np
import pytest


from helper_functions import SplitDates
from helper_functions import CountNulls

# def test_null_count():

data = ['2015-02-04', '2016-03-05']
dt_series = pd.to_datetime(pd.Series(data))
dt = SplitDates(dt_series)

# print(dt.series)

def test_split_dates():
    df = dt.split_dates()
    assert len(df.columns) == 3
    assert list(df.columns) == ['month', 'day', 'year']

