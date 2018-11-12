import numpy as np
import pandas as pd
from pandas import DataFrame, Series


def create_df(index, columns):
    data = [[k + str(i) for k in columns] for i in index]
    return DataFrame(data=data, index=index, columns=columns)


def new_df(index, columns):
    data = {k: [k + str(i) for i in index] for k in columns}
    return DataFrame(data, index)


if __name__ == '__main__':
    d1 = create_df(list('1234'), list('ABCDE'))
    d2 = create_df(list('45'), list('DFG'))

    n1 = np.random.randint(15, size=(3, 3))
    n2 = np.random.randint(15, size=(3, 2))
    print(np.concatenate((n1, n2), axis=1))  # 行数相同， 列可不同， 列合并

    n1 = np.random.randint(10, size=(3, 3))
    n2 = np.random.randint(10, size=(2, 3))
    print(np.concatenate((n1, n2), axis=0))  # 列数相同， 行可不同， 行合并，连接
