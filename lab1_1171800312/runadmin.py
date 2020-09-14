import sys
import admin
import studentreg
import teacherreg
import selectcourse
import updategrade
import querygrade
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox

def startApp(a):
    if a==1:
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = admin.Ui_MainWindow()
        # 向主窗口上添加控件
        ui.setupUi(mainWindow)
        mainWindow.setWindowTitle("院系管理")
        mainWindow.show()
        sys.exit(app.exec_())
    elif a==2:
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = studentreg.Ui_MainWindow()
        # 向主窗口上添加控件
        ui.setupUi(mainWindow)
        mainWindow.setWindowTitle("学生注册")
        mainWindow.show()
        sys.exit(app.exec_())
    elif a==3:
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = teacherreg.Ui_MainWindow()
        # 向主窗口上添加控件
        ui.setupUi(mainWindow)
        mainWindow.setWindowTitle("教师注册")
        mainWindow.show()
        sys.exit(app.exec_())
    elif a==4:
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = selectcourse.Ui_MainWindow()
        # 向主窗口上添加控件
        ui.setupUi(mainWindow)
        mainWindow.setWindowTitle("学生选课")
        mainWindow.show()
        sys.exit(app.exec_())
    elif a==5:
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = updategrade.Ui_MainWindow()
        # 向主窗口上添加控件
        ui.setupUi(mainWindow)
        mainWindow.setWindowTitle("上成绩")
        mainWindow.show()
        sys.exit(app.exec_())
    elif a==6:
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        ui = querygrade.Ui_MainWindow()
        # 向主窗口上添加控件
        ui.setupUi(mainWindow)
        mainWindow.setWindowTitle("查成绩")
        mainWindow.show()
        sys.exit(app.exec_())
    else:
        print("error")