# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_before(object):
    def setupUi(self, before):
        before.setObjectName("before")
        before.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(before)
        self.centralwidget.setObjectName("centralwidget")
        self.selectsql = QtWidgets.QComboBox(self.centralwidget)
        self.selectsql.setGeometry(QtCore.QRect(30, 60, 551, 31))
        self.selectsql.setObjectName("selectsql")
        self.selectsql.addItem("")
        self.selectsql.addItem("")
        self.selectsql.addItem("")
        self.go = QtWidgets.QPushButton(self.centralwidget)
        self.go.setGeometry(QtCore.QRect(690, 60, 81, 31))
        self.go.setObjectName("go")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 100, 741, 431))
        self.textEdit.setObjectName("textEdit")
        self.input = QtWidgets.QPushButton(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(600, 60, 81, 31))
        self.input.setObjectName("input")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 741, 31))
        self.lineEdit.setObjectName("lineEdit")
        before.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(before)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        before.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(before)
        self.statusbar.setObjectName("statusbar")
        before.setStatusBar(self.statusbar)

        self.retranslateUi(before)
        QtCore.QMetaObject.connectSlotsByName(before)

    def retranslateUi(self, before):
        _translate = QtCore.QCoreApplication.translate
        before.setWindowTitle(_translate("before", "MainWindow"))
        self.selectsql.setItemText(0, _translate("before", "SELECT [ ENAME = ’Mary’ & DNAME = ’Research’ ] ( EMPLOYEE JOIN DEPARTMENT )"))
        self.selectsql.setItemText(1, _translate("before", "PROJECTION [ BDATE ] ( SELECT [ ENAME = ’John’ & DNAME = ’ Research’ ] ( EMPLOYEE JOIN DEPARTMENT) )"))
        self.selectsql.setItemText(2, _translate("before", "SELECT [ ESSN = ’01’ ] ( PROJECTION [ ESSN, PNAME ] ( WORKS_ON JOIN PROJECT ) )"))
        self.go.setText(_translate("before", "执行"))
        self.textEdit.setHtml(_translate("before", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">语法树</p></body></html>"))
        self.input.setText(_translate("before", "导入"))

