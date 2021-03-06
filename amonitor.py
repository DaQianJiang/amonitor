# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'amonitor.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from MatplotlibWidget import MatplotlibWidget

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(504, 374)
        self.pakagename = QtWidgets.QLabel(Form)
        self.pakagename.setGeometry(QtCore.QRect(30, 30, 60, 16))
        self.pakagename.setObjectName("pakagename")

        self.packege_name = QtWidgets.QLineEdit(Form)
        self.packege_name.setGeometry(QtCore.QRect(90, 30, 131, 21))
        self.packege_name.setObjectName("packege_name")

        self.updateetime = QtWidgets.QLabel(Form)
        self.updateetime.setGeometry(QtCore.QRect(260, 30, 60, 16))
        self.updateetime.setObjectName("updateetime")

        self.update_time = QtWidgets.QLineEdit(Form)
        self.update_time.setGeometry(QtCore.QRect(330, 30, 81, 21))
        self.update_time.setObjectName("update_time")
        self.start_btn = QtWidgets.QPushButton(Form)
        self.start_btn.setGeometry(QtCore.QRect(80, 70, 81, 32))
        self.start_btn.setObjectName("start_btn")
        self.stop_btn = QtWidgets.QPushButton(Form)
        self.stop_btn.setGeometry(QtCore.QRect(210, 70, 81, 32))
        self.stop_btn.setObjectName("stop_btn")
        self.clear_btn = QtWidgets.QPushButton(Form)
        self.clear_btn.setGeometry(QtCore.QRect(330, 70, 71, 32))
        self.clear_btn.setObjectName("clear_btn")
        self.graph = QtWidgets.QLabel(Form)
        self.graph.setGeometry(QtCore.QRect(20, 190, 60, 16))
        self.graph.setObjectName("graph")

        #self.graph_photo = QtWidgets.QGraphicsView(Form)
        self.graph_photo = MatplotlibWidget(Form)
        self.graph_photo.setGeometry(QtCore.QRect(70, 150, 381, 201))
        self.graph_photo.setObjectName("graph_photo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pakagename.setText(_translate("Form", "应用名称"))
        self.updateetime.setText(_translate("Form", "更新时间"))
        self.start_btn.setText(_translate("Form", "开始"))
        self.stop_btn.setText(_translate("Form", "结束"))
        self.clear_btn.setText(_translate("Form", "清除"))
        self.graph.setText(_translate("Form", "图表"))
