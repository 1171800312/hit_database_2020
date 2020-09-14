# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updategrade.ui'
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
        MainWindow.resize(742, 531)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chaxunchengji = QtWidgets.QPushButton(self.centralwidget)
        self.chaxunchengji.setGeometry(QtCore.QRect(570, 60, 75, 23))
        self.chaxunchengji.setObjectName("chaxunchengji")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 50, 31, 39))
        self.label_2.setObjectName("label_2")
        self.jiaoshihao = QtWidgets.QLineEdit(self.centralwidget)
        self.jiaoshihao.setGeometry(QtCore.QRect(160, 60, 101, 20))
        self.jiaoshihao.setText("")
        self.jiaoshihao.setObjectName("jiaoshihao")
        self.chengji = QtWidgets.QLabel(self.centralwidget)
        self.chengji.setGeometry(QtCore.QRect(160, 110, 461, 201))
        self.chengji.setObjectName("chengji")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 64, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 50, 31, 39))
        self.label.setObjectName("label")
        self.mima = QtWidgets.QLineEdit(self.centralwidget)
        self.mima.setGeometry(QtCore.QRect(300, 60, 101, 20))
        self.mima.setText("")
        self.mima.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mima.setObjectName("mima")
        self.xiugaichengji = QtWidgets.QPushButton(self.centralwidget)
        self.xiugaichengji.setGeometry(QtCore.QRect(380, 350, 75, 23))
        self.xiugaichengji.setObjectName("xiugaichengji")
        self.kehao = QtWidgets.QLineEdit(self.centralwidget)
        self.kehao.setGeometry(QtCore.QRect(447, 61, 101, 20))
        self.kehao.setText("")
        self.kehao.setObjectName("kehao")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 360, 47, 13))
        self.label_3.setObjectName("label_3")
        self.xuehao = QtWidgets.QLineEdit(self.centralwidget)
        self.xuehao.setGeometry(QtCore.QRect(220, 360, 113, 20))
        self.xuehao.setObjectName("xuehao")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 390, 191, 71))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 390, 47, 13))
        self.label_6.setObjectName("label_6")
        self.chengji_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.chengji_2.setGeometry(QtCore.QRect(220, 390, 113, 20))
        self.chengji_2.setObjectName("chengji_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def seecourses(self):
        tnumber = (self.jiaoshihao.text())
        password = (self.mima.text())
        coursenum = self.kehao.text()
        print(tnumber,password,coursenum)
        try:
            conn = sqlite3.connect("school.db")
            cursor = conn.cursor()
            # 注意单双引号
            cursor.execute("PRAGMA foreign_keys = ON")
            #cursor.execute('insert into course values(?,?,?,?)',(cno,credit,tno,coursename))
            cursor.execute("select password from teacher where tno = ?",(tnumber,))
            res = cursor.fetchone()
            if res== None:
                self.chengji.setText("教师不存在")
                return
            if res[0] == password:
                self.chengji.setText("输入正确")
                cursor.execute("select sno,sname,grade from course natural join sel natural join student where cno=? and tno=?",(coursenum,tnumber))
                result = ""
                for temp in cursor.fetchall():
                    result+=("学号：")
                    result+=str(temp[0])
                    result+=("  姓名：")
                    result+=str(temp[1])
                    result+=("  当前成绩：")
                    if temp[2] == -1:
                        result+="未上成绩"
                    else:
                        result+=str(temp[2])

                    result+=str("\n")
                  #  result+=("课程号："+str(temp[0])+"  课程名："+str(temp[3])+"  学分："+str(temp[1])+"  任课教师："+str(temp[4])+"\n")
                self.chengji.setText(result)
            else:
                self.chengji.setText("密码错误")
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
    def modifygrade(self):
        sno = (self.xuehao.text())
        grade = (self.chengji_2.text())
        cno = (self.kehao.text())
        try:
            conn = sqlite3.connect("school.db")
            cursor = conn.cursor()
            # 注意单双引号
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute('update sel set grade=? where sno=? and cno=?',(grade,sno,cno))
            # cursor.execute("select * from user")
            # print(cursor.fetchone())
            # print(cursor.fetchmany(100))
            conn.commit()
            cursor.close()
            conn.close()
            self.label_5.setText("成功")
            self.seecourses()
        except sqlite3.IntegrityError:
            traceback.print_exc()
            self.edureaction.setText("不满足完整性约束")
            conn.rollback()
            cursor.close()
            conn.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chaxunchengji.setText(_translate("MainWindow", "查询成绩"))
        self.chaxunchengji.clicked.connect(self.seecourses)
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.chengji.setText(_translate("MainWindow", "输入教师号和密码查看学生成绩"))
        self.label_4.setText(_translate("MainWindow", "课号"))
        self.label.setText(_translate("MainWindow", "教师号"))
        self.xiugaichengji.setText(_translate("MainWindow", "修改成绩"))
        self.xiugaichengji.clicked.connect(self.modifygrade)
        self.label_3.setText(_translate("MainWindow", "学号"))
        self.label_5.setText(_translate("MainWindow", "修改情况将在这里显示"))
        self.label_6.setText(_translate("MainWindow", "成绩"))

