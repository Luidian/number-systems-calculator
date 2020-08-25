# coding: utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
from PyQt5.QtCore import  QSize
from PyQt5.QtGui import QFont, QEnterEvent, QPainter, QColor, QPen
import sys
from calculation import convert_base

class Calc(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calc, self).__init__()
        self.setWindowFlags( QtCore.Qt.WindowCloseButtonHint )
        self.setWindowIcon(QtGui.QIcon('calculator.jpg'))
        self.setWindowTitle('Calculator')
        self.setFixedSize(QSize(426, 440))
        # self.setBackgroundRole()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(palette.Window, QColor(120, 20, 230))
        self.setPalette(palette)

        self.ui.lineEdit_2.setReadOnly(True)
        # Заполнение comboBox
        for i in range(2, 17):
            self.ui.Of.addItem(str(i))
            self.ui.In.addItem(str(i))
        
        self.initUi()
        
    def initUi(self):
        # Кнопочки
        self.ui.zero.clicked.connect(lambda: self.entry_field(0))
        self.ui.one.clicked.connect(lambda: self.entry_field(1))
        self.ui.two.clicked.connect(lambda: self.entry_field(2))
        self.ui.three.clicked.connect(lambda: self.entry_field(3))
        self.ui.four.clicked.connect(lambda: self.entry_field(4))
        self.ui.five.clicked.connect(lambda: self.entry_field(5))
        self.ui.six.clicked.connect(lambda: self.entry_field(6))
        self.ui.seven.clicked.connect(lambda: self.entry_field(7))
        self.ui.eight.clicked.connect(lambda: self.entry_field(8))
        self.ui.nine.clicked.connect(lambda: self.entry_field(9))
        self.ui.A.clicked.connect(lambda: self.entry_field('A'))
        self.ui.B.clicked.connect(lambda: self.entry_field('B'))
        self.ui.C.clicked.connect(lambda: self.entry_field('C'))
        self.ui.D.clicked.connect(lambda: self.entry_field('D'))
        self.ui.F.clicked.connect(lambda: self.entry_field('F'))
        # self.ui.Point.clicked.connect(lambda: self.entry_field('.'))
        self.ui.Backsp.clicked.connect(lambda: self.ui.lineEdit.backspace())
        self.ui.CE.clicked.connect(lambda: self.ui.lineEdit.clear())
        self.ui.execute.clicked.connect(lambda: self.convert())

    # Заполнение поля ввода
    def entry_field(self, sumb):
        if self.ui.lineEdit.text() == "Введите число" or self.ui.lineEdit.text() == "0":
            self.ui.lineEdit.clear()
        # print(self.ui.lineEdit.text())
        self.ui.lineEdit.setText(self.ui.lineEdit.text() + str(sumb))

    # Заполненеи поля результата
    def output_field(self, res):
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_2.setText(str(res))

    # Ф-я расчета
    def convert(self):
        try:
            self.output_field(convert_base(self.ui.lineEdit.text(), self.ui.In.currentIndex()+2, self.ui.Of.currentIndex()+2))
        except:
            self.output_field("Выбра неверная с/c")

# ------------------------------------------------------------        


app = QtWidgets.QApplication([])

application = Calc()
application.show()

sys.exit(app.exec())