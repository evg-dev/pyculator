# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from decimal import Decimal
from math import sqrt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMessageBox, QAction, qApp, QApplication,
                             QPushButton, QLineEdit, QMainWindow)

number = 0.0
new_number = 0.0
total = 0.0
operator = ''
new_operator = ''

count = 0  # Count call result

op_count = False  # operators cycle
res_count = False  # result cycle

opr_signal = False  # Signals operators keypress
key_signals = False  # Signals numbers keypress
func_signals = False  #Signal from functions


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit pyculator')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 230, 310)
        self.setFixedSize(230, 310)
        self.setWindowTitle('Menu')

        self.line = QLineEdit(self)
        self.line.move(5, 35)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        self.line.resize(220, 25)
        self.line.setText('0')

        zero = QPushButton('0', self)
        zero.move(5, 245)
        zero.resize(40, 40)

        one = QPushButton('1', self)
        one.move(5, 200)
        one.resize(40, 40)

        two = QPushButton('2', self)
        two.move(50, 200)
        two.resize(40, 40)

        three = QPushButton('3', self)
        three.move(95, 200)
        three.resize(40, 40)

        four = QPushButton('4', self)
        four.move(5, 155)
        four.resize(40, 40)

        five = QPushButton('5', self)
        five.move(50, 155)
        five.resize(40, 40)

        six = QPushButton('6', self)
        six.move(95, 155)
        six.resize(40, 40)

        seven = QPushButton('7', self)
        seven.move(5, 110)
        seven.resize(40, 40)

        eight = QPushButton('8', self)
        eight.move(50, 110)
        eight.resize(40, 40)

        nine = QPushButton('9', self)
        nine.move(95, 110)
        nine.resize(40, 40)

        point = QPushButton('.', self)
        point.move(50, 245)
        point.resize(40, 40)
        point.clicked.connect(self.Point)

        switch = QPushButton('+/-', self)
        switch.move(95, 245)
        switch.resize(40, 40)
        switch.clicked.connect(self.Switch)

        plus = QPushButton('+', self)
        plus.resize(40, 85)
        plus.move(140, 200)

        minus = QPushButton('-', self)
        minus.move(185, 155)
        minus.resize(40, 40)

        divide = QPushButton('/', self)
        divide.move(140, 110)
        divide.resize(40, 40)

        multiply = QPushButton('*', self)
        multiply.move(140, 155)
        multiply.resize(40, 40)

        sqrt = QPushButton("√", self)
        sqrt.move(185, 65)
        sqrt.resize(40, 40)
        sqrt.clicked.connect(self.Sqrt)

        squared = QPushButton("x²", self)
        squared.move(185, 110)
        squared.resize(40, 40)
        squared.clicked.connect(self.Squared)

        result = QPushButton('=', self)
        result.resize(40, 85)
        result.move(185, 200)
        result.clicked.connect(self.Result)

        c = QPushButton("C", self)
        c.move(5, 65)
        c.resize(85, 40)
        c.setStyleSheet("color:red;")
        c.clicked.connect(self.C)

        ce = QPushButton("CE", self)
        ce.move(95, 65)
        ce.resize(40, 40)
        ce.setStyleSheet("color:red;")
        ce.clicked.connect(self.CE)

        back = QPushButton("Back", self)
        back.move(140, 65)
        back.resize(40, 40)
        back.clicked.connect(self.Back)

        nums = [zero, one, two, three, four, five, six, seven, eight, nine]

        operators = [divide, multiply, minus, plus]

        for i in nums:
            i.setStyleSheet("color:blue;")
            i.clicked.connect(self.Nums)

        for i in operators:
            i.setStyleSheet("color:green;")
            i.clicked.connect(self.Operators)

        self.setWindowTitle('Pyculator')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Quit', "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Enter:
            return self.Result()

        if e.key() == Qt.Key_Escape:
            return self.C()

        if e.key() == Qt.Key_Backspace:
            return self.Back()

        if e.key() == Qt.Key_Period:
            return self.Point()

        if e.key() == Qt.Key_0:
            return self.Nums('0')

        if e.key() == Qt.Key_1:
            return self.Nums('1')

        if e.key() == Qt.Key_2:
            return self.Nums('2')

        if e.key() == Qt.Key_3:
            return self.Nums('3')

        if e.key() == Qt.Key_4:
            return self.Nums('4')

        if e.key() == Qt.Key_5:
            return self.Nums('5')

        if e.key() == Qt.Key_6:
            return self.Nums('6')

        if e.key() == Qt.Key_7:
            return self.Nums('7')

        if e.key() == Qt.Key_8:
            return self.Nums('8')

        if e.key() == Qt.Key_9:
            return self.Nums('9')

        if e.key() == Qt.Key_Asterisk:
            return self.Operators('*')

        if e.key() == Qt.Key_Plus:
            return self.Operators('+')

        if e.key() == Qt.Key_Minus:
            return self.Operators('-')

        if e.key() == Qt.Key_Slash:
            return self.Operators('/')

    def Nums(self, n):
        global opr_signal
        global key_signals

        sender = self.sender()

        if self.line.text() == '0':
            self.line.clear()

        if n:
            num = n
        else:
            num = sender.text()

        if not opr_signal:
            self.line.setText(self.line.text() + num)
        else:
            self.line.setText(num)
            opr_signal = False
            op_count = False

        key_signals = True

    def Point(self):
        if "." not in self.line.text():
            self.line.setText(self.line.text() + ".")

    def Switch(self):
        num = Decimal(self.line.text())
        num = -num
        self.line.setText(str(num))

    def Opr(self):
        global new_number
        global total
        global operator
        global number

        if operator == "+":
            total = Decimal(number) + Decimal(new_number)

        if operator == "-":
            total = Decimal(number) - Decimal(new_number)

        if operator == "*":
            total = Decimal(number) * Decimal(new_number)

        if operator == "/":
            try:
                total = Decimal(number) / Decimal(new_number)
            except Exception:
                total = '0'

    def Operators(self, o):
        global number
        global total
        global operator
        global new_operator
        global new_number

        global count

        global op_count
        global res_count

        global key_signals
        global opr_signal

        sender = self.sender()

        if op_count:

            new_number = self.line.text()

            if o:
                new_operator = o
            else:
                new_operator = sender.text()

            if (not opr_signal):
                self.Opr()
                self.line.setText(str(total))
                number = total

            operator = new_operator
        else:
            if o:
                operator = o
            else:
                operator = sender.text()

            number = self.line.text()
            op_count = True

        opr_signal = True
        key_signals = False
        res_count = False
        count = 0

    def Result(self):
        global number
        global new_number
        global total
        global operator
        global new_number

        global count

        global op_count
        global res_count

        global opr_signal
        global key_signals
        global func_signals

        if operator:

            if (not res_count):
                new_number = self.line.text()

            if func_signals:
                number = self.line.text()

            if (key_signals & (count > 1)):
                number = self.line.text()

            self.Opr()
            self.line.setText(str(total))
            number = total
            res_count = True
            count += 1

        opr_signal = True
        key_signals = False
        func_signals = False

    def Sqrt(self):
        global func_signals

        num = Decimal(self.line.text())
        try:
            num = sqrt(num)
        except Exception:
            num = '0'
        self.line.setText(str(num))
        func_signals = True

    def Squared(self):
        global func_signals

        num = Decimal(self.line.text())
        num **= 2
        self.line.setText(str(num))

        func_signals = True

    def C(self):
        global number
        global new_number
        global total
        global operator
        global new_operator

        global op_count
        global res_count

        global opr_signal
        global key_signals
        global func_signals

        number = 0
        new_number = 0
        total = 0

        opr_signal = False
        key_signals = False
        op_count = False
        res_count = False
        func_signals = False
        operator = ''
        new_operator = ''
        self.line.setText('0')

    def CE(self):
        self.line.setText('0')

    def Back(self):
        global func_signals

        # Bug. Not work from keyboard before GUI first!
        num = self.line.text()[:-1]
        if len(num) == 0:
            num = '0'
        self.line.setText(num)

        func_signals = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
