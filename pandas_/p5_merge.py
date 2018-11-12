import numpy as np
import pandas as pd
from pandas import DataFrame


if __name__ == '__main__':
    s1 = pd.read_excel('关系表.xlsx', sheet_name=1)
    print(s1)

    s2 = pd.read_excel('关系表.xlsx', sheet_name=2)
    print(s2)

    print(pd.merge(s1, s2, how='outer'))