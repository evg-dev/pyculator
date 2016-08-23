# !/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from decimal import Decimal
from math import sqrt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMessageBox, QAction, qApp, QApplication,
                             QPushButton, QLineEdit, QMainWindow)


class Data:

    number = 0.0
    new_number = 0.0
    total = 0.0
    operator = ''
    new_operator = ''


class Signals:

    count = 0  # Count call result

    op_count = False  # operators cycle
    res_count = False  # result cycle

    opr_signal = False  # Signals operators keypress
    key_signals = False  # Signals numbers keypress
    func_signals = False  # Signal from functions

    @staticmethod
    def op_count_true():
        Signals.op_count = True
        return Signals.op_count

    @staticmethod
    def op_count_false():
        Signals.op_count = False
        return Signals.op_count

    @staticmethod
    def res_count_true():
        Signals.res_count = True
        return Signals.res_count

    @staticmethod
    def res_count_false():
        Signals.res_count = False
        return Signals.res_count

    @staticmethod
    def opr_signal_true():
        Signals.opr_signal = True
        return Signals.opr_signal

    @staticmethod
    def opr_signal_false():
        Signals.opr_signal = False
        return Signals.opr_signal

    @staticmethod
    def key_signals_true():
        Signals.key_signals = True
        return Signals.key_signals

    @staticmethod
    def key_signals_false():
        Signals.key_signals = False
        return Signals.key_signals

    @staticmethod
    def func_signals_true():
        Signals.func_signals = True
        return Signals.func_signals

    @staticmethod
    def func_signals_false():
        Signals.func_signals = False
        return Signals.func_signals


class GUI(QMainWindow):

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


class Main(Data, Signals, GUI):

    def __init__(self):
        super().__init__()

    def Nums(self, n):

        sender = self.sender()

        if self.line.text() == '0':
            self.line.clear()

        if n:
            num = n
        else:
            num = sender.text()

        if not Signals.opr_signal:
            self.line.setText(self.line.text() + num)
        else:
            self.line.setText(num)
            Signals.opr_signal_false()
            Signals.op_count_false()

        Signals.key_signals_true()

    def Point(self):
        if "." not in self.line.text():
            self.line.setText(self.line.text() + ".")

    def Switch(self):
        num = Decimal(self.line.text())
        num = -num
        self.line.setText(str(num))

    def Opr(self):

        if Data.operator == "+":
            Data.total = Decimal(Data.number) + Decimal(Data.new_number)

        if Data.operator == "-":
            Data.total = Decimal(Data.number) - Decimal(Data.new_number)

        if Data.operator == "*":
            Data.total = Decimal(Data.number) * Decimal(Data.new_number)

        if Data.operator == "/":
            try:
                Data.total = Decimal(Data.number) / Decimal(Data.new_number)
            except Exception:
                Data.total = '0'

    def Operators(self, o):

        sender = self.sender()

        if Signals.op_count:

            Data.new_number = self.line.text()

            if o:
                Data.new_operator = o
            else:
                Data.new_operator = sender.text()

            if (not Signals.opr_signal):
                self.Opr()
                self.line.setText(str(Data.total))
                Data.number = Data.total

            Data.operator = Data.new_operator
        else:
            if o:
                Data.operator = o
            else:
                Data.operator = sender.text()

            Data.number = self.line.text()
            Signals.op_count_true()

        Signals.opr_signal_true()
        Signals.key_signals_false()
        Signals.res_count_false()
        Signals.count = 0

    def Result(self):

        if Data.operator:

            if (not Signals.res_count):
                Data.new_number = self.line.text()

            if Signals.func_signals:
                Data.number = self.line.text()

            if (Signals.key_signals & (Signals.count > 1)):
                Data.number = self.line.text()

            self.Opr()
            self.line.setText(str(Data.total))
            Data.number = Data.total
            Signals.res_count_true()
            Signals.count += 1

        Signals.opr_signal_true()
        Signals.key_signals_false()
        Signals.func_signals_false()

    def Sqrt(self):
        num = Decimal(self.line.text())
        try:
            num = sqrt(num)
        except Exception:
            num = '0'
        self.line.setText(str(num))
        Signals.func_signals_true()

    def Squared(self):
        num = Decimal(self.line.text())
        num **= 2
        self.line.setText(str(num))

        Signals.func_signals_true()

    def C(self):

        Data.number = 0
        Data.new_number = 0
        Data.total = 0
        Data.operator = ''
        Data.new_operator = ''

        Signals.opr_signal_false()
        Signals.key_signals_false()
        Signals.op_count_false()
        Signals.res_count_false()
        Signals.func_signals_false()

        self.line.setText('0')

    def CE(self):
        self.line.setText('0')

    def Back(self):
        # Bug. Not work from keyboard before GUI first!
        num = self.line.text()[:-1]
        if len(num) == 0:
            num = '0'
        self.line.setText(num)

        Signals.func_signals_true()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
