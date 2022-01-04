import re
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def main5():
    # read
    dict_data = {
        'x': [],
        'y': [],
        'z': []
    }
    with open('./data5/data.txt') as f:
        dict_data['x'] = f.readline().strip().split()
        dict_data['y'] = [float(i) for i in f.readline().strip().split()]
        dict_data['z'] = [float(i) for i in f.readline().strip().split()]

    # create
    fig = plt.figure()

    # ax1
    ax1 = fig.add_subplot(111)
    ax1.bar(dict_data['x'], dict_data['y'], label='计算时间', width=0.5, alpha=0.5)
    ax1.set_xlabel('OpenMP线程数')
    ax1.set_ylabel('GCR计算时间（s）')

    # ax2
    ax2 = ax1.twinx()  # this is the important function
    ax2.plot(dict_data['x'], dict_data['z'], label='加速比', marker='o', alpha=0.5)
    ax2.set_ylabel('加速比')
    fig.legend(loc=1, bbox_to_anchor=(1, 0.8), bbox_transform=ax1.transAxes)

    # save
    plt.savefig('img/5.png', dpi=500, bbox_inches='tight')


if __name__ == '__main__':
    main5()
