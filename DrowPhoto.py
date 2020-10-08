import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from ExcelOprate import excelOprate
import matplotlib.animation as animation


class Graph(object):
    data_value = excelOprate().read_exceldata("cpu占用")
    def __init__(self):
        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        self.fig = plt.figure(figsize=(5, 4), dpi=100)
        self.ax1 = self.fig.add_subplot()
        #self.ax2 = self.fig.add_subplot(2,2,3)

    def graphPhoto(self):
        plt.xlabel('Date')
        plt.ylabel('CPU占用率')

        # self.ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        xdata = self.data_value.col_values(0)
        ydata =self.data_value.col_values(1)
        self.ax1.plot(xdata,ydata)
        for label in self.ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
        plt.show()

    # def animate(i):
        #x.append(data_value.col_values(0))
        #y.append(data_value.col_values(1))
    # ax1.clear()
    # ax1.plot(x, y)
    # ani = FuncAnimation(plt.gcf(), animate, interval=1000)
    # plt.show()



if __name__ == '__main__':
    gra = Graph()

