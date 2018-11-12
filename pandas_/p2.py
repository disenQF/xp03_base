import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


if __name__ == '__main__':

    gyy = plt.imread('images/gyy2.jpg')
    print(gyy.shape)

    ms4 = plt.imread('images/ms4.jpg')
    print(ms4.shape)

    gyy2 = gyy[:220, :329]
    plt.imsave('gm.jpg', np.concatenate((gyy2, ms4), axis=0))  # 行合
    plt.imsave('gm2.jpg', np.concatenate((gyy2, ms4), axis=1))  # 列合

    # plt.imsave('gm3.jpg', pd.concat((gyy2, ms4), axis=0))  # 列合

