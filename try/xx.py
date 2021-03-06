
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import time
import csv
import os

ROOTPATH = os.path.abspath('..')
plt.style.use('fivethirtyeight')

x=[]
y=[]
i=0
fig = plt.figure(figsize=(5, 4), dpi=100)
ax1 = fig.add_subplot(2,2,1)


def animate(i):
    with open(os.path.join(ROOTPATH,'example.txt'),'r') as files:
        reader = csv.reader(files)
        for line in reader:
            x.append(line[0])
            y.append(line[1])
    ax1.clear()
    ax1.plot(x, y)


# def animate(i):
#     # i表示的是经历过的"时间", 即每调用一次animate函数, i的值会自动加一
#     # 我们从一个动态生成数据的csv文件中获取数据来模拟动态数据
#     data = csv.reader()
#     # 获得该动态数据的所有列的所有数据(当前生成的), 到下一次运行时该数据如果变动了, 绘出来的图形自然也变动了
#     x = data['x_value']
#     y1 = data['total_1']
#     y2 = data['total_2']
#     # plt对象的cla方法: clear axes: 清除当前轴线(前面说过axes对象表示的是plt整个figure对象下面的一个绘图对象, 一个figure可以有多个axes, 其实就是当前正在绘图的实例).
#     # 我们可以不清除当前的axes而沿用前面的axes, 但这样会产生每次绘出来的图形都有很大的变化(原因是重新绘制的时候,颜色,坐标等都重新绘制,可能不在同一个地方了,所以看上去会时刻变化).
#     # 因此必须要清除当前axes对象,来重新绘制.
#     plt.cla()
#     plt.plot(x, y1, label='Channel 1')
#     plt.plot(x, y2, label='Channel 2')
#     plt.legend(loc='upper left')
#     plt.tight_layout()
#
#
# # FuncAnimation可以根据给定的interval(时间间隔, ms为单位)一直重复调用某个函数来进行绘制, 从而模拟出实时数据的效果.
ani = FuncAnimation(fig, animate, interval=1000)

plt.show()

# if __name__ == '__main__':
#     write_data()
