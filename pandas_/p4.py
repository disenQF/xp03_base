import numpy as np
import pandas as pd
from pandas import DataFrame


if __name__ == '__main__':
    data = np.random.randint(1, 100, size=(2, 3))
    index = ['张三', '李四']
    columns = ['Python', 'H5', 'Java']

    d = DataFrame(data=data, index=index, columns=columns)
    print(d)

    d2 = DataFrame(data={'计算机': [90, 100]}, index=index)
    print(d2)

    d3 = pd.concat((d, d2), axis=1)
    print(d3)

    columns2 = d3.columns
    index2 = ['王老五']
    data2 = np.random.randint(100, size=(1,4))
    d4 = DataFrame(data=data2, index=index2, columns= columns2)
    print(d4)

    print(pd.concat((d3, d4)))