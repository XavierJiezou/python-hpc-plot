import matplotlib.pyplot as plt
import numpy as np
import os
import re


def main2():
    dict_data = {}
    for name in sorted(os.listdir('data2/'), key=lambda x: int(x.split('.')[0])):
        path = 'data2/'+name
        with open(path) as f:
            x = []
            y = []
            for item in f.readlines():
                t_x = re.findall(r'Size: (.*?) ', item)[0]
                t_y = re.findall(r'Gflop/s: (.*?) ', item)[0]
                x.append(int(t_x))
                y.append(float(t_y))
            dict_data[name[:-4]] = {
                'x': x,
                'y': y
            }
    plt.figure(figsize=(6000/500, 4000/500), dpi=500)
    plt.title('DGEMM and OpenMp Performance Comparision')
    for key in dict_data:
        plt.xlim(0, 1064)
        plt.ylim(0, 150)
        plt.xticks([2**i for i in range(5, 11)] )
        plt.plot(dict_data[key]['x'], dict_data[key]['y'], label=key)
    plt.xlabel('Matrix Dimension')
    plt.ylabel('GFLOPS')
    plt.legend()
    plt.grid()
    plt.savefig('img/2.png', dpi=500, bbox_inches='tight')


if __name__ == '__main__':
    main2()
