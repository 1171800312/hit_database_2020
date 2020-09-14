# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'querygrade.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sqlite3
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 477)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.xuehao = QtWidgets.QLineEdit(self.centralwidget)
        self.xuehao.setGeometry(QtCore.QRect(90, 20, 158, 20))
        self.xuehao.setObjectName("xuehao")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 31, 39))
        self.label.setObjectName("label")
        self.mima = QtWidgets.QLineEdit(self.centralwidget)
        self.mima.setGeometry(QtCore.QRect(310, 20, 158, 20))
        self.mima.setText("")
        self.mima.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mima.setObjectName("mima")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 31, 39))
        self.label_2.setObjectName("label_2")
        self.chachengji = QtWidgets.QPushButton(self.centralwidget)
        self.chachengji.setGeometry(QtCore.QRect(500, 20, 75, 23))
        self.chachengji.setObjectName("chachengji")
        self.chengjixianshi = QtWidgets.QLabel(self.centralwidget)
        self.chengjixianshi.setGeometry(QtCore.QRect(90, 70, 451, 201))
        self.chengjixianshi.setObjectName("chengjixianshi")
        self.chengjifenxi = QtWidgets.QLabel(self.centralwidget)
        self.chengjifenxi.setGeometry(QtCore.QRect(90, 320, 431, 71))
        self.chengjifenxi.setObjectName("chengjifenxi")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def seecourses(self):
        snumber = (self.xuehao.text())
        password = (self.mima.text())
        try:
            conn = sqlite3.connect("school.db")
            cursor = conn.cursor()
            # 注意单双引号
            cursor.execute("PRAGMA foreign_keys = ON")
            #cursor.execute('insert into course values(?,?,?,?)',(cno,credit,tno,coursename))
            cursor.execute("select password from student where sno = ?",(snumber,))
            res = cursor.fetchone()
            if res== None:
                self.chengjixianshi.setText("学生不存在")
                return
            if res[0] == password:
                self.chengjixianshi.setText("输入正确")
                cursor.execute("select * from course natural join teacher natural join sel where sno = ?",(snumber,))
                result = ""
                for temp in cursor.fetchall():
                    result+=("课程号："+str(temp[0])+"  课程名："+str(temp[3])+"  学分："+str(temp[1])+"  任课教师："+str(temp[4]))
                    if temp[9]==-1:
                        result+=("  未上成绩")
                    else:
                        result+=("  成绩："+str(temp[9]))
                    result+="\n"
                self.chengjixianshi.setText(result)
            else:
                self.chengjixianshi.setText("密码错误")
           # print(cursor.fetchall())
            conn.commit()
            cursor.close()
            conn.close()
        except sqlite3.IntegrityError:
            traceback.print_exc()
            self.kexuankecheng.setText("完整性约束不符合")
            conn.rollback()
            cursor.close()
            conn.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "学号"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.chachengji.setText(_translate("MainWindow", "查成绩"))
        self.chachengji.clicked.connect(self.seecourses)
        self.chengjixianshi.setText(_translate("MainWindow", "成绩将显示在这里"))
        self.chengjifenxi.setText(_translate("MainWindow", "成绩分析"))

