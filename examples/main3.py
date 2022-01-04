import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
import numpy as np
import os
import re


def main3():
    # read
    dict_data = {
        'x': [],
        'y': []
    }
    with open('./data/data3/data.txt') as f:
        for line in f.readlines():
            line = line.strip().split(' ')
            x = line[0]
            y = line[1]
            dict_data['x'].append(x)
            dict_data['y'].append(float(y))

    # bar
    plt.bar(dict_data['x'], dict_data['y'], label='Helmholtz', width=0.3, alpha=0.5)
    plt.xlabel('进程数')
    plt.ylabel('求解赫姆霍兹方程所占比例')
    def to_percent(temp, position):
        return '%1.2f'%(temp) + '%'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    plt.legend()
    
    # save
    plt.savefig('imgs/3.png', dpi=500, bbox_inches='tight')


if __name__ == '__main__':
    main3()
