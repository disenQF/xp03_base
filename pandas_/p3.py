from pandas_.p1 import new_df
import pandas as pd
import numpy as np


if __name__ == '__main__':
    d1 = new_df(list('1234'), list('ABCD'))
    d2 = new_df(list('345'), list('CD'))

    d3 = pd.concat((d1, d2), axis=1, join_axes=[pd.Index(['3', '4'])])
    print(d3)