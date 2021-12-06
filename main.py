import matplotlib.pyplot as plt
import numpy as np
import os


def main():
    dict_data = {}
    for name in os.listdir('data/'):
        path = 'data/'+name
        with open(path) as f:
            x = []
            y = []
            for item in f.readlines():
                each = item.split(' ')
                x.append(int(each[0]))
                y.append(float(each[1]))
            dict_data[name[:-4]] = {
                'x': x,
                'y': y
            }
    plt.figure(figsize=(6000/500, 4000/500), dpi=500)
    plt.title('Performance Comparision')
    for key in dict_data:
        plt.xlim(0, 1064)
        plt.ylim(0, 32)
        plt.xticks([2**i for i in range(5, 11)] )
        plt.plot(dict_data[key]['x'], dict_data[key]['y'], label=key)
    plt.xlabel('Matrix Dimension')
    plt.ylabel('GFLOPS')
    plt.legend()
    plt.grid()
    plt.savefig('img/1.png', dpi=500)


if __name__ == '__main__':
    main()
