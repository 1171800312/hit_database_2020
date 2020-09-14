# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectcourse.ui'
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
        MainWindow.resize(645, 401)
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
        self.chaxunkexuankecheng = QtWidgets.QPushButton(self.centralwidget)
        self.chaxunkexuankecheng.setGeometry(QtCore.QRect(500, 20, 75, 23))
        self.chaxunkexuankecheng.setObjectName("chaxunkexuankecheng")
        self.kexuankecheng = QtWidgets.QLabel(self.centralwidget)
        self.kexuankecheng.setGeometry(QtCore.QRect(90, 70, 461, 201))
        self.kexuankecheng.setObjectName("kexuankecheng")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 310, 47, 13))
        self.label_4.setObjectName("label_4")
        self.kehao = QtWidgets.QLineEdit(self.centralwidget)
        self.kehao.setGeometry(QtCore.QRect(150, 310, 113, 20))
        self.kehao.setObjectName("kehao")
        self.xuanke = QtWidgets.QPushButton(self.centralwidget)
        self.xuanke.setGeometry(QtCore.QRect(300, 310, 75, 23))
        self.xuanke.setObjectName("xuanke")
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
                self.kexuankecheng.setText("学生不存在")
                return
            if res[0] == password:
                self.kexuankecheng.setText("输入正确")
                #体现嵌套查询
                cursor.execute("select * from course natural join teacher where dept in(select dno from student where sno = ?)",(snumber,))
                result = ""
                for temp in cursor.fetchall():
                    result+=("课程号："+str(temp[0])+"  课程名："+str(temp[3])+"  学分："+str(temp[1])+"  任课教师："+str(temp[4])+"\n")
                self.kexuankecheng.setText(result)
            else:
                self.kexuankecheng.setText("密码错误")
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
    def selectcourse(self):
        sno = self.xuehao.text()
        cno = self.kehao.text()
        try:
            conn = sqlite3.connect("school.db")
            cursor = conn.cursor()
            # 注意单双引号
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("select * from sel where sno =? and cno = ?",(sno,cno))
            res = cursor.fetchall()
            if res!=[]:
                cursor.execute("delete from sel where sno = ? and cno = ?",(sno,cno))
                self.xuanke.setText("退课成功")
            else:
                cursor.execute('insert into sel values(?,?,?)', (sno,cno,-1))
                self.xuanke.setText("选课成功")
            # cursor.execute("select * from user")
            # print(cursor.fetchone())
            # print(cursor.fetchmany(100))
            conn.commit()
            cursor.close()
            conn.close()

        except sqlite3.IntegrityError:
            traceback.print_exc()
            self.xuanke.setText("选课失败")
            conn.rollback()
            cursor.close()
            conn.close()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "学号"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.chaxunkexuankecheng.setText(_translate("MainWindow", "查询可选课程"))
        self.chaxunkexuankecheng.clicked.connect(self.seecourses)
        self.kexuankecheng.setText(_translate("MainWindow", "输入学号和密码，可查询可选课程"))
        self.label_4.setText(_translate("MainWindow", "课号"))
        self.xuanke.setText(_translate("MainWindow", "选课"))
        self.xuanke.clicked.connect(self.selectcourse)
