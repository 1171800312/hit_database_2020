# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import traceback

class Ui_MainWindow(object):
    def adddepartment(self):
        dname  = self.deptname.text()
        dno = self.deptnum.text()
        try:
            conn = sqlite3.connect("school.db")
            cursor = conn.cursor()
            # 注意单双引号
            cursor.execute('insert into dept values(?,?)',(dno,dname))
            # cursor.execute("select * from user")
            # print(cursor.fetchone())
            # print(cursor.fetchmany(100))
            cursor.execute("")
            conn.commit()
            cursor.close()
            conn.close()
            self.label_5.setText("追加"+dname+"成功")
        except Exception:
            traceback.print_exc()
            self.label_5.setText("不满足完整性约束")
            conn.rollback()
            cursor.close()
            conn.close()

    def addclass(self):
        clsno = self.clsnum.text()
        clsname= self.clsname.text()
        try:
            conn = sqlite3.connect("school.db")
            cursor = conn.cursor()
            # 注意单双引号
            cursor.execute('insert into cls values(?,?)', (clsno, clsname))#要更改插入的表
            # cursor.execute("select * from user")
            # print(cursor.fetchone())
            # print(cursor.fetchmany(100))
            conn.commit()
            cursor.close()
            conn.close()
            self.label_5.setText("追加" + clsname + "成功")
        except Exception:
            traceback.print_exc()
            self.label_5.setText("不满足完整性约束")
            conn.rollback()
            cursor.close()
            conn.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(378, 368)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 90, 160, 80))
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
        self.adddept = QtWidgets.QPushButton(self.formLayoutWidget)
        self.adddept.setObjectName("adddept")
        self.adddept.clicked.connect(self.adddepartment)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.adddept)
        self.deptnum = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.deptnum.setObjectName("deptnum")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.deptnum)
        self.deptname = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.deptname.setObjectName("deptname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.deptname)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(100, 200, 160, 80))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.addcls = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.addcls.setObjectName("addcls")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.addcls)
        self.addcls.clicked.connect(self.addclass)
        self.clsnum = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.clsnum.setObjectName("clsnum")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.clsnum)
        self.clsname = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.clsname.setObjectName("clsname")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.clsname)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 20, 180, 50))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def getinfo(self):
        try:
            conn = sqlite3.connect("school.db")
            #指定访问的数据库文件名称
            cursor = conn.cursor()
            cursor.execute("SELECT count(*),dept.dno FROM dept left outer NATURAL join student group by dept.dno having count(*)>=3")
            #把这一块换成你的SQL语句
            res =(cursor.fetchall())
            #fetchall函数可以返回所有的查询结果，以元组的格式体现
            tag =""
            #输出的临时字符串
            for temp in res:
                tag+=("系号："+str(temp[1])+"  当前注册人数："+str(temp[0])+"\n")
                #把fetchall得到的结果转换成字符串
            conn.commit()
            #保存更改
            cursor.close()
            #关闭数据库
            conn.close()
            self.label_5.setText(tag)
        except Exception:
            traceback.print_exc()
            self.label_5.setText("程序出现异常")
            conn.rollback()
            cursor.close()
            conn.close()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "系号"))
        self.label_2.setText(_translate("MainWindow", "系名"))
        self.adddept.setText(_translate("MainWindow", "追加系"))
        self.label_3.setText(_translate("MainWindow", "班号"))
        self.label_4.setText(_translate("MainWindow", "班级名称"))
        self.addcls.setText(_translate("MainWindow", "追加班级"))
        self.label_5.setText(_translate("MainWindow", "教务视角"))
        self.getinfo()

