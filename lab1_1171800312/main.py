# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import runadmin
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from tkinter.simpledialog import askinteger
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664, 487)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 140, 431, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.shangchengji = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.shangchengji.setMaximumSize(QtCore.QSize(150, 50))
        self.shangchengji.setObjectName("shangchengji")
        self.gridLayout.addWidget(self.shangchengji, 2, 1, 1, 1)
        self.chachengji = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.chachengji.setMaximumSize(QtCore.QSize(150, 50))
        self.chachengji.setObjectName("chachengji")
        self.gridLayout.addWidget(self.chachengji, 3, 1, 1, 1)
        self.jiaoshizhuce = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.jiaoshizhuce.setMaximumSize(QtCore.QSize(150, 50))
        self.jiaoshizhuce.setObjectName("jiaoshizhuce")
        self.gridLayout.addWidget(self.jiaoshizhuce, 3, 0, 1, 1)
        self.xueshengxuanke = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.xueshengxuanke.setMaximumSize(QtCore.QSize(150, 50))
        self.xueshengxuanke.setObjectName("xueshengxuanke")
        self.gridLayout.addWidget(self.xueshengxuanke, 0, 1, 1, 1)
        self.xueshengzhuce = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.xueshengzhuce.setMaximumSize(QtCore.QSize(150, 50))
        self.xueshengzhuce.setObjectName("xueshengzhuce")
        self.gridLayout.addWidget(self.xueshengzhuce, 2, 0, 1, 1)
        self.yuanxiguanli = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.yuanxiguanli.setMaximumSize(QtCore.QSize(150, 50))
        self.yuanxiguanli.setObjectName("yuanxiguanli")
        self.gridLayout.addWidget(self.yuanxiguanli, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 50, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def updategrade(self):
        runadmin.startApp(5)
    def querygrade(self):
        print(6)
    def teacherreg(self):
        print(3)
    def selectcourse(self):
        print(4)
    def studentreg(self):
        print(2)
    def deptadmin(self):
        print(1)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.shangchengji.setText(_translate("MainWindow", "上成绩"))
        self.shangchengji.clicked.connect(self.updategrade)
        self.chachengji.setText(_translate("MainWindow", "查成绩"))
        self.chachengji.clicked.connect(self.querygrade)
        self.jiaoshizhuce.setText(_translate("MainWindow", "教师注册"))
        self.jiaoshizhuce.clicked.connect(self.teacherreg)
        self.xueshengxuanke.setText(_translate("MainWindow", "学生选课"))
        self.xueshengxuanke.clicked.connect(self.selectcourse)
        self.xueshengzhuce.setText(_translate("MainWindow", "学生注册"))
        self.xueshengzhuce.clicked.connect(self.studentreg)
        self.yuanxiguanli.setText(_translate("MainWindow", "院系管理"))
        self.yuanxiguanli.clicked.connect(self.deptadmin)
        self.label.setText(_translate("MainWindow", "学生成绩管理系统 by WJP"))

#var_int = askinteger("hello","world")
#runadmin.startApp(var_int)


import tkinter as tk

# 设置窗口

window = tk.Tk()
window.title('学生管理系统by WJP')
window.geometry('350x200')
l = tk.Label(window,text="请选择功能：\n 1.院系管理 \n 2.学生注册 \n 3.教师注册 \n 4.学生选课 \n 5.上成绩 \n 6.查成绩")
l.pack()
e = tk.Entry()
e.pack()
def insert_point():
    var1 = int(e.get())
    print(var1)
    runadmin.startApp(var1)
b1 = tk.Button(text='启动', width=20, height=2, command=insert_point)
b1.pack()
window.mainloop()

