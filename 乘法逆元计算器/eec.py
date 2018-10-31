# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QIcon
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 344)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.x = QtWidgets.QLabel(self.centralwidget)
        self.x.setGeometry(QtCore.QRect(30, 30, 54, 12))
        self.x.setObjectName("x")
        self.y = QtWidgets.QLabel(self.centralwidget)
        self.y.setGeometry(QtCore.QRect(30, 90, 54, 12))
        self.y.setObjectName("y")
        self.s = QtWidgets.QLabel(self.centralwidget)
        self.s.setGeometry(QtCore.QRect(20, 150, 91, 20))
        self.s.setObjectName("s")
        self.t = QtWidgets.QLabel(self.centralwidget)
        self.t.setGeometry(QtCore.QRect(23, 210, 91, 20))
        self.t.setObjectName("t")
        self.x_value = QtWidgets.QLineEdit(self.centralwidget)
        self.x_value.setGeometry(QtCore.QRect(140, 30, 451, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.x_value.setFont(font)
        self.x_value.setObjectName("x_value")
        self.y_value = QtWidgets.QLineEdit(self.centralwidget)
        self.y_value.setGeometry(QtCore.QRect(140, 90, 451, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.y_value.setFont(font)
        self.y_value.setObjectName("y_value")
        self.s_value = QtWidgets.QLineEdit(self.centralwidget)
        # self.s_value.setEnabled(False)
        self.s_value.setGeometry(QtCore.QRect(140, 150, 451, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.s_value.setFont(font)
        self.s_value.setObjectName("s_value")
        self.t_value = QtWidgets.QLineEdit(self.centralwidget)
        # self.t_value.setEnabled(False)
        self.t_value.setGeometry(QtCore.QRect(140, 210, 451, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.t_value.setFont(font)
        self.t_value.setObjectName("t_value")
        self.cal_Button = QtWidgets.QPushButton(self.centralwidget)
        self.cal_Button.setGeometry(QtCore.QRect(520, 250, 75, 23))
        self.cal_Button.setObjectName("cal_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "乘法逆元计算器"))
        MainWindow.setWindowIcon(QIcon("logo.png"))
        self.x.setText(_translate("MainWindow", "x"))
        self.y.setText(_translate("MainWindow", "y"))
        self.s.setText(_translate("MainWindow", "x模y的乘法逆元"))
        self.t.setText(_translate("MainWindow", "y模x的乘法逆元"))
        self.cal_Button.setText(_translate("MainWindow", "计算"))

        self.s_value.setReadOnly(True)
        self.t_value.setReadOnly(True)


    def show_warning_message(self):
        """弹出异常消息弹窗"""
        QMessageBox.information(self, "warning", "输入数据有误",QMessageBox.Yes)


    def setupFunction(self):
        """添加逻辑功能"""
        self.cal_Button.clicked.connect(self.calculator)

    def check_input(self,x,y):
        """参数检查"""
        if x < 2 and y < 2:
            return False
        if self.gcd(x,y) == 1:
            return True
        else:
            return False

    def gcd(self,x,y):
        """求两个数的最大公因数"""
        while y != 0:
            x, y = y, x % y
        return x


    def calculator(self):
        """实现计算功能"""
        x = int(self.x_value.text())
        y = int(self.y_value.text())
        if min(x, y) == x:
            tmp = x
            x = y
            y = tmp
        if self.check_input(x,y):
            s0 = 1
            t0 = 0
            s1 = 0
            t1 = 1
            q = divmod(x, y)[0]
            r = divmod(x, y)[1]
            s2 = s0 - q * s1
            t2 = t0 - q * t1
            while r != 0:
                tmp_y = r
                q = divmod(y, r)[0]
                r = divmod(y, r)[1]
                s3 = s1 - q * s2
                t3 = t1 - q * t2
                s1 = s2
                t1 = t2
                s2 = s3
                t2 = t3
                y = tmp_y
            self.s_value.setText(str(s1))
            self.t_value.setText(str(t1))
        else:
            self.show_warning_message()
            self.x_value.clear()
            self.y_value.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setupFunction()
    MainWindow.show()
    sys.exit(app.exec_())