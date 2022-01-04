import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
import numpy as np
import os
import re


def main4():
    # read
    dict_data = {
        'x': [],
        'y': []
    }
    with open('./data4/data.txt') as f:
        for line in f.readlines():
            line = line.strip().split(' ')
            x = line[0]
            y = line[1]
            dict_data['x'].append(x)
            dict_data['y'].append(float(y))

    # pie
    plt.pie(dict_data['y'], labels=dict_data['x'], autopct="%1.0f%%")

    # save
    plt.savefig('img/4.png', dpi=500, bbox_inches='tight')


if __name__ == '__main__':
    main4()
