# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacherreg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(376, 381)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 40, 160, 126))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.zhigonghao = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.zhigonghao.setObjectName("zhigonghao")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.zhigonghao)
        self.jiaoshixingming = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.jiaoshixingming.setObjectName("jiaoshixingming")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.jiaoshixingming)
        self.jiaoshixingbie = QtWidgets.QComboBox(self.formLayoutWidget)
        self.jiaoshixingbie.setObjectName("jiaoshixingbie")
        self.jiaoshixingbie.addItem("")
        self.jiaoshixingbie.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.jiaoshixingbie)
        self.mima = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.mima.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mima.setObjectName("mima")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.mima)
        self.suoshuxihao = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.suoshuxihao.setObjectName("suoshuxihao")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.suoshuxihao)
        self.jiaoshizhuce = QtWidgets.QLabel(self.centralwidget)
        self.jiaoshizhuce.setGeometry(QtCore.QRect(100, 170, 91, 31))
        self.jiaoshizhuce.setObjectName("jiaoshizhuce")
        self.zhuce = QtWidgets.QPushButton(self.centralwidget)
        self.zhuce.setGeometry(QtCore.QRect(180, 170, 75, 23))
        self.zhuce.setObjectName("zhuce")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(100, 200, 160, 80))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.kechenghao = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.kechenghao.setObjectName("kechenghao")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.kechenghao)
        self.kechengming = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.kechengming.setObjectName("kechengming")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.kechengming)
        self.xuefen = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.xuefen.setObjectName("xuefen")
        self.xuefen.addItem("")
        self.xuefen.addItem("")
        self.xuefen.addItem("")
        self.xuefen.addItem("")
        self.xuefen.addItem("")
        self.xuefen.addItem("")
        self.xuefen.addItem("")
        self.xuefen.addItem("")
        self.xuefen.addItem("")
        self.xuefen.addItem("")
        self.xuefen.addItem("")
        self.xuefen.addItem("")
        self.xuefen.addItem("")
        self.xuefen.addItem("")
        self.xuefen.addItem("")
        self.xuefen.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.xuefen)
        self.jiaoshikaike = QtWidgets.QLabel(self.centralwidget)
        self.jiaoshikaike.setGeometry(QtCore.QRect(100, 280, 81, 31))
        self.jiaoshikaike.setObjectName("jiaoshikaike")
        self.kaike = QtWidgets.QPushButton(self.centralwidget)
        self.kaike.setGeometry(QtCore.QRect(180, 280, 75, 23))
        self.kaike.setObjectName("kaike")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 376, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def teacherregister(self):
        tno = (self.zhigonghao.text())
        tname = (self.jiaoshixingming.text())
        tsex = (self.jiaoshixingbie.currentText())
        password = (self.mima.text())
        dept = (self.suoshuxihao.text())
        try:
            conn = sqlite3.connect("school.db")
            cursor = conn.cursor()
            # 注意单双引号
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute('insert into teacher values(?,?,?,?,?)',(tno,tname,tsex,password,dept))
            # cursor.execute("select * from user")
            # print(cursor.fetchone())
            # print(cursor.fetchmany(100))
            conn.commit()
            cursor.close()
            conn.close()
            self.jiaoshizhuce.setText("追加"+tname+"成功")
        except sqlite3.IntegrityError:
            traceback.print_exc()
            self.jiaoshizhuce.setText("不满足完整性约束")
            conn.rollback()
            cursor.close()
            conn.close()
    def setupcourse(self):
        tno = (self.zhigonghao.text())
        cno = self.kechenghao.text()
        credit = self.xuefen.currentText()
        coursename = self.kechengming.text()
        try:
            conn = sqlite3.connect("school.db")
            cursor = conn.cursor()
            # 注意单双引号
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute('insert into course values(?,?,?,?)',(cno,credit,tno,coursename))
            # cursor.execute("select * from user")
            # print(cursor.fetchone())
            # print(cursor.fetchmany(100))
            conn.commit()
            cursor.close()
            conn.close()
            self.jiaoshikaike.setText("追加"+cno+"成功")
        except sqlite3.IntegrityError:
            traceback.print_exc()
            self.jiaoshikaike.setText("不满足完整性约束")
            conn.rollback()
            cursor.close()
            conn.close()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "职工号"))
        self.label_2.setText(_translate("MainWindow", "教师姓名"))
        self.label_3.setText(_translate("MainWindow", "教师性别"))
        self.label_4.setText(_translate("MainWindow", "密码"))
        self.label_5.setText(_translate("MainWindow", "所属系号"))
        self.jiaoshixingbie.setItemText(0, _translate("MainWindow", "男"))
        self.jiaoshixingbie.setItemText(1, _translate("MainWindow", "女"))
        self.jiaoshizhuce.setText(_translate("MainWindow", "教师注册->"))
        self.zhuce.setText(_translate("MainWindow", "注册"))
        self.zhuce.clicked.connect(self.teacherregister)
        self.label_7.setText(_translate("MainWindow", "课程号"))
        self.label_8.setText(_translate("MainWindow", "课程名"))
        self.label_9.setText(_translate("MainWindow", "学分"))
        self.xuefen.setItemText(0, _translate("MainWindow", "0.5"))
        self.xuefen.setItemText(1, _translate("MainWindow", "1"))
        self.xuefen.setItemText(2, _translate("MainWindow", "1.5"))
        self.xuefen.setItemText(3, _translate("MainWindow", "2"))
        self.xuefen.setItemText(4, _translate("MainWindow", "2.5"))
        self.xuefen.setItemText(5, _translate("MainWindow", "3"))
        self.xuefen.setItemText(6, _translate("MainWindow", "3.5"))
        self.xuefen.setItemText(7, _translate("MainWindow", "4"))
        self.xuefen.setItemText(8, _translate("MainWindow", "4.5"))
        self.xuefen.setItemText(9, _translate("MainWindow", "5"))
        self.xuefen.setItemText(10, _translate("MainWindow", "5.5"))
        self.xuefen.setItemText(11, _translate("MainWindow", "6"))
        self.xuefen.setItemText(12, _translate("MainWindow", "6.5"))
        self.xuefen.setItemText(13, _translate("MainWindow", "7"))
        self.xuefen.setItemText(14, _translate("MainWindow", "7.5"))
        self.xuefen.setItemText(15, _translate("MainWindow", "8"))
        self.jiaoshikaike.setText(_translate("MainWindow", "教师开课->"))
        self.kaike.setText(_translate("MainWindow", "开课"))
        self.kaike.clicked.connect(self.setupcourse)

