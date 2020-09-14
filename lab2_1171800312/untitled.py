# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 780)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 10, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 81, 16))
        self.label_2.setObjectName("label_2")
        self.sel1 = QtWidgets.QComboBox(self.centralwidget)
        self.sel1.setGeometry(QtCore.QRect(230, 60, 73, 22))
        self.sel1.setObjectName("sel1")
        self.sel1.addItem("")
        self.sel1.addItem("")
        self.sel2 = QtWidgets.QComboBox(self.centralwidget)
        self.sel2.setGeometry(QtCore.QRect(340, 60, 73, 22))
        self.sel2.setObjectName("sel2")
        self.sel2.addItem("")
        self.sel2.addItem("")
        self.sel2.addItem("")
        self.sel2.addItem("")
        self.sel3 = QtWidgets.QLineEdit(self.centralwidget)
        self.sel3.setGeometry(QtCore.QRect(450, 60, 113, 22))
        self.sel3.setObjectName("sel3")
        self.selexe = QtWidgets.QPushButton(self.centralwidget)
        self.selexe.setGeometry(QtCore.QRect(650, 60, 93, 28))
        self.selexe.setObjectName("selexe")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 110, 81, 16))
        self.label_3.setObjectName("label_3")
        self.proj1 = QtWidgets.QComboBox(self.centralwidget)
        self.proj1.setGeometry(QtCore.QRect(230, 110, 73, 22))
        self.proj1.setObjectName("proj1")
        self.proj1.addItem("")
        self.proj1.addItem("")
        self.proj2 = QtWidgets.QComboBox(self.centralwidget)
        self.proj2.setGeometry(QtCore.QRect(340, 110, 73, 22))
        self.proj2.setObjectName("proj2")
        self.proj2.addItem("")
        self.proj2.addItem("")
        self.proj2.addItem("")
        self.proj2.addItem("")
        self.projexe = QtWidgets.QPushButton(self.centralwidget)
        self.projexe.setGeometry(QtCore.QRect(650, 110, 93, 28))
        self.projexe.setObjectName("projexe")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 160, 81, 16))
        self.label_4.setObjectName("label_4")
        self.join1 = QtWidgets.QComboBox(self.centralwidget)
        self.join1.setGeometry(QtCore.QRect(230, 160, 181, 21))
        self.join1.setObjectName("join1")
        self.join1.addItem("")
        self.join1.addItem("")
        self.join1.addItem("")
        self.joinexe = QtWidgets.QPushButton(self.centralwidget)
        self.joinexe.setGeometry(QtCore.QRect(650, 160, 93, 28))
        self.joinexe.setObjectName("joinexe")
        self.log = QtWidgets.QTextEdit(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(40, 210, 371, 481))
        self.log.setReadOnly(True)
        self.log.setObjectName("log")
        self.res = QtWidgets.QTextEdit(self.centralwidget)
        self.res.setGeometry(QtCore.QRect(440, 210, 371, 481))
        self.res.setReadOnly(True)
        self.res.setObjectName("res")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(740, 700, 75, 23))
        self.save.setObjectName("save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 21))
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
        self.label.setText(_translate("MainWindow", "缓冲区管理"))
        self.label_2.setText(_translate("MainWindow", "选择操作："))
        self.sel1.setItemText(0, _translate("MainWindow", "R"))
        self.sel1.setItemText(1, _translate("MainWindow", "S"))
        self.sel2.setItemText(0, _translate("MainWindow", "A"))
        self.sel2.setItemText(1, _translate("MainWindow", "B"))
        self.sel2.setItemText(2, _translate("MainWindow", "C"))
        self.sel2.setItemText(3, _translate("MainWindow", "D"))
        self.sel3.setText(_translate("MainWindow", "40"))
        self.selexe.setText(_translate("MainWindow", "执行"))
        self.label_3.setText(_translate("MainWindow", "投影操作："))
        self.proj1.setItemText(0, _translate("MainWindow", "R"))
        self.proj1.setItemText(1, _translate("MainWindow", "S"))
        self.proj2.setItemText(0, _translate("MainWindow", "A"))
        self.proj2.setItemText(1, _translate("MainWindow", "B"))
        self.proj2.setItemText(2, _translate("MainWindow", "C"))
        self.proj2.setItemText(3, _translate("MainWindow", "D"))
        self.projexe.setText(_translate("MainWindow", "执行"))
        self.label_4.setText(_translate("MainWindow", "连接操作："))
        self.join1.setItemText(0, _translate("MainWindow", "nest_loop_join"))
        self.join1.setItemText(1, _translate("MainWindow", "sort_merge_join"))
        self.join1.setItemText(2, _translate("MainWindow", "hash_join"))
        self.joinexe.setText(_translate("MainWindow", "执行"))
        self.log.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">操作日志</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.res.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">操作结果</p></body></html>"))
        self.save.setText(_translate("MainWindow", "结果保存"))

