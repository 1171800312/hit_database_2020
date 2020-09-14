import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import untitled2
from syntaxtree import SyntaxTree

employee = ["ESSN" "ENAME", "DNO"]
department = ["DNO", "DNAME"]
project = ["PNAME", "PNO","DNO"],
works_on = ["ESSN", "PNO"]

def parse(sql_statement):
    sql = sql_statement.split()
    execute_tree = SyntaxTree()
    index = 0
    while True:
        if index >= len(sql):
            break
        #处理一元运算符
        elif sql[index] == 'SELECT' or sql[index] == 'PROJECTION':
            execute_tree.operator = sql[index]
            index += 2  # 从[开始到]里面的全部记录下来
            condition = ''
            while sql[index] != ']':
                condition += sql[index]
                condition += ' '
                index += 1
            index += 1
            execute_tree.condition = condition
        #处理二元运算符
        elif sql[index] == 'JOIN':
            # 连接操作需要创建子树，所以分开写
            execute_tree.operator = sql[index]
            execute_tree.left_child = SyntaxTree()
            execute_tree.left_child.attribute = sql[index - 1]
            execute_tree.right_child = SyntaxTree()
            execute_tree.right_child.attribute = sql[index + 1]
            index += 1
        #处理子查询，进行递归
        elif sql[index] == '(':
            index += 1
            statement = ''
            while index < len(sql) and sql[index] != ')':
                statement += sql[index]
                statement += ' '
                index += 1
            index += 1
            execute_tree.left_child = parse(statement)
        else:
            index += 1

    return execute_tree


def search(sql):
    sql = sql.split()
    if sql[0] in employee:
        return "EMPLOYEE"
    elif sql[0] in department:
        return "DEPARTMENT"
    elif sql[0] in project:
        return "PROJECT"
    elif sql[0] in works_on:
        return "WORKS_ON"
    return None


def optimize(syntax_tree, sql):
    if syntax_tree.operator == 'SELECT':
        condition = syntax_tree.condition
        #拆开条件,并把条件向下传递
        sql = condition.split('&')
        relation = []
        for i in range(len(sql)):
            if search(sql[i]) is not None:
                relation.append(search(sql[i]))
        syntax_tree = optimize(syntax_tree.left_child, sql)
    elif syntax_tree.operator == 'PROJECTION':
        syntax_tree.left_child = optimize(syntax_tree.left_child, sql)
    elif syntax_tree.operator == 'JOIN':
        first_tree = SyntaxTree()
        first_tree.operator = 'SELECT'
        first_tree.condition = sql[0]
        first_tree.left_child = syntax_tree.left_child
        syntax_tree.left_child = first_tree
        if len(sql) == 1:
            return syntax_tree
        second_tree = SyntaxTree()
        second_tree.operator = 'SELECT'
        second_tree.condition = sql[1]
        second_tree.right_child = syntax_tree.right_child
        syntax_tree.right_child = second_tree
    return syntax_tree


def print_tree(syntax_tree):
    global indent
    if syntax_tree.operator != '':
        ui.textEdit.append(" "*indent+syntax_tree.operator+"  "+syntax_tree.condition)
    else:
        ui.textEdit.append(" "*indent+syntax_tree.attribute.replace(")",""))
    if syntax_tree.left_child is not None:
        indent = indent+2
        print_tree(syntax_tree.left_child)
        indent = indent-2
    if syntax_tree.right_child is not None:
        indent = indent+2
        print_tree(syntax_tree.right_child)
        indent = indent-2
def input():
    ui.lineEdit.setText(ui.selectsql.currentText())
def execute():
    sql = ui.lineEdit.text()
    etree1 = parse(sql)
    ui.textEdit.clear()
    ui.textEdit.append("优化前：")
    print_tree(etree1)
    ui.textEdit.append('优化后：')
    otree1 = optimize(etree1, '')
    print_tree(otree1)
if __name__ == '__main__':
    sql1 = "SELECT [ ENAME = ’Mary’ & DNAME = ’Research’ ] ( EMPLOYEE JOIN DEPARTMENT )"
    sql2 = "PROJECTION [ BDATE ] ( SELECT [ ENAME = ’John’ & DNAME = ’ Research’ ] ( EMPLOYEE JOIN DEPARTMENT) )"
    sql3 = "SELECT [ ESSN = ’01’ ] ( PROJECTION [ ESSN, PNAME ] ( WORKS_ON JOIN PROJECT ) )"
    indent = 0
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = untitled2.Ui_before()
    # 向主窗口上添加控件
    ui.setupUi(mainWindow)
    ui.go.clicked.connect(execute)
    ui.input.clicked.connect(input)
    mainWindow.setWindowTitle("查询优化器")
    mainWindow.show()
    sys.exit(app.exec_())
