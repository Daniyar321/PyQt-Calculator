# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calcul.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(359, 345)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 80, 360, 261))
        self.gridLayoutWidget.setMinimumSize(QtCore.QSize(0, 35))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_0.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 4, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 3, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_tk = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_tk.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_tk.setObjectName("pushButton_tk")
        self.gridLayout.addWidget(self.pushButton_tk, 4, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_mul = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_mul.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.gridLayout.addWidget(self.pushButton_mul, 2, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)
        self.pushButton_sub = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_sub.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.gridLayout.addWidget(self.pushButton_sub, 1, 3, 1, 1)
        self.pushButton_div = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_div.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout.addWidget(self.pushButton_div, 3, 3, 1, 1)
        self.pushButton_c = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_c.setObjectName("pushButton_c")
        self.gridLayout.addWidget(self.pushButton_c, 0, 0, 1, 1)
        self.pushButton_mc = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_mc.setObjectName("pushButton_mc")
        self.gridLayout.addWidget(self.pushButton_mc, 0, 1, 1, 1)
        self.pushButton_m = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_m.setObjectName("pushButton_m")
        self.gridLayout.addWidget(self.pushButton_m, 0, 2, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 0, 3, 1, 1)
        self.pushButton_eq = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_eq.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_eq.setObjectName("pushButton_eq")
        self.gridLayout.addWidget(self.pushButton_eq, 4, 2, 1, 2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 20, 341, 51))
        self.lcdNumber.setObjectName("lcdNumber")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 359, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_tk.setText(_translate("MainWindow", "."))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_mul.setText(_translate("MainWindow", "*"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_sub.setText(_translate("MainWindow", "-"))
        self.pushButton_div.setText(_translate("MainWindow", "/"))
        self.pushButton_c.setText(_translate("MainWindow", "C"))
        self.pushButton_mc.setText(_translate("MainWindow", "MC"))
        self.pushButton_m.setText(_translate("MainWindow", "M"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_eq.setText(_translate("MainWindow", "="))


