import matplotlib
from PyQt5.QtCore import QTimer

from ExcelOprate import excelOprate

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy  as np
import sys

# 绘图的空白界面
class MymplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(221) # 多界面绘图
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding, QSizePolicy.Expanding
                                   )
        FigureCanvas.updateGeometry(self)

    def start_static_plot(self):
        self.axes.clear()
        self.data_value = excelOprate().read_exceldata("cpu占用")
        plt.xlabel('Date')
        plt.ylabel('CPU占用率')

        # self.ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        xdata = self.data_value.col_values(0)
        ydata =self.data_value.col_values(1)
        self.axes.plot(xdata,ydata)
        for label in self.axes.xaxis.get_ticklabels():
            label.set_rotation(45)
        #plt.show()
        self.axes.grid(True)
        self.draw()

    # 为何要加参数
    def start_dynamic_plot(self, *args, **kwargs):
        timer = QTimer(self)
        timer.timeout.connect(self.update_fig)
        timer.start(1000)

    def update_fig(self):
        self.axes.clear()
        self.data_value = excelOprate().read_exceldata("cpu占用")
        plt.xlabel('Date')
        plt.ylabel('CPU占用率')

        # self.ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        xdata = self.data_value.col_values(0)
        ydata =self.data_value.col_values(1)
        self.axes.plot(xdata,ydata)
        for label in self.axes.xaxis.get_ticklabels():
            label.set_rotation(45)
        #plt.show()
        self.axes.grid(True)
        self.draw()


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MymplCanvas(self, width=5, height=4, dpi=100)
        #self.mpl.start_static_plot() # 如果你想要初始化的时候就呈现静态图，请把这行注释去掉
        #self.mpl.start_dynamic_plot() # 如果你想要初始化的时候就呈现动态图，请把这行注释去掉
        self.mpl_ntb = NavigationToolbar(self.mpl, self)  # 添加完整的 toolbar

        self.layout.addWidget(self.mpl)
        # self.layout.addWidget(self.mpl_ntb)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    #ui.mpl.start_static_plot()  # 测试静态图效果
    ui.mpl.start_dynamic_plot() # 测试动态图效果
    ui.show()
    sys.exit(app.exec_())