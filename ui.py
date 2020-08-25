# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(426, 477)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color:     rgb(230,230,230);\n"
"}\n"
"QMenuBar{\n"
"    background-color:     rgb(230,230,230);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(250,250,250);\n"
"    width: 75px;\n"
"    height: 50px;\n"
"    font-size: 14px;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:     rgb(128,128,128);\n"
"}\n"
"\n"
"QComboBox{\n"
"    background-color:     rgb(230,230,230);\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLabel{\n"
"    font-size: 14px;\n"
"}\n"
"QLineEdit{\n"
"    background-color: rgb(230,230,230);\n"
"    font-size: 14px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 60, 281, 30))
        self.lineEdit_2.setMaxLength(5000)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.In = QtWidgets.QComboBox(self.centralwidget)
        self.In.setGeometry(QtCore.QRect(50, 60, 71, 30))
        self.In.setObjectName("In")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 401, 321))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.five = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.five.setObjectName("five")
        self.gridLayout_3.addWidget(self.five, 3, 1, 1, 1)
        self.zero = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.zero.setObjectName("zero")
        self.gridLayout_3.addWidget(self.zero, 5, 1, 1, 1)
        self.seven = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.seven.setObjectName("seven")
        self.gridLayout_3.addWidget(self.seven, 2, 0, 1, 1)
        self.execute = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.execute.setObjectName("execute")
        self.gridLayout_3.addWidget(self.execute, 5, 3, 1, 1)
        self.eight = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.eight.setObjectName("eight")
        self.gridLayout_3.addWidget(self.eight, 2, 1, 1, 1)
        self.CE = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.CE.setObjectName("CE")
        self.gridLayout_3.addWidget(self.CE, 5, 0, 1, 1)
        self.one = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.one.setObjectName("one")
        self.gridLayout_3.addWidget(self.one, 4, 0, 1, 1)
        self.two = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.two.setObjectName("two")
        self.gridLayout_3.addWidget(self.two, 4, 1, 1, 1)
        self.four = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.four.setObjectName("four")
        self.gridLayout_3.addWidget(self.four, 3, 0, 1, 1)
        self.Point = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Point.setObjectName("Point")
        self.gridLayout_3.addWidget(self.Point, 5, 2, 1, 1)
        self.nine = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.nine.setObjectName("nine")
        self.gridLayout_3.addWidget(self.nine, 2, 2, 1, 1)
        self.six = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.six.setObjectName("six")
        self.gridLayout_3.addWidget(self.six, 3, 2, 1, 1)
        self.three = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.three.setObjectName("three")
        self.gridLayout_3.addWidget(self.three, 4, 2, 1, 1)
        self.A = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.A.setObjectName("A")
        self.gridLayout_3.addWidget(self.A, 0, 0, 1, 1)
        self.B = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.B.setObjectName("B")
        self.gridLayout_3.addWidget(self.B, 0, 1, 1, 1)
        self.C = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.C.setObjectName("C")
        self.gridLayout_3.addWidget(self.C, 0, 2, 1, 1)
        self.F = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.F.setObjectName("F")
        self.gridLayout_3.addWidget(self.F, 3, 3, 1, 1)
        self.D = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.D.setObjectName("D")
        self.gridLayout_3.addWidget(self.D, 2, 3, 1, 1)
        self.Backsp = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Backsp.setObjectName("Backsp")
        self.gridLayout_3.addWidget(self.Backsp, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 30))
        self.label.setObjectName("label")
        self.Of = QtWidgets.QComboBox(self.centralwidget)
        self.Of.setGeometry(QtCore.QRect(50, 10, 71, 30))
        self.Of.setObjectName("Of")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 10, 281, 30))
        self.lineEdit.setMaxLength(500)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 31, 30))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 426, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_2.setText(_translate("MainWindow", "Результат"))
        self.five.setText(_translate("MainWindow", "5"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.execute.setText(_translate("MainWindow", "="))
        self.eight.setText(_translate("MainWindow", "8"))
        self.CE.setText(_translate("MainWindow", "CE"))
        self.one.setText(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.four.setText(_translate("MainWindow", "4"))
        self.Point.setText(_translate("MainWindow", "."))
        self.nine.setText(_translate("MainWindow", "9"))
        self.six.setText(_translate("MainWindow", "6"))
        self.three.setText(_translate("MainWindow", "3"))
        self.A.setText(_translate("MainWindow", "A"))
        self.B.setText(_translate("MainWindow", "B"))
        self.C.setText(_translate("MainWindow", "C"))
        self.F.setText(_translate("MainWindow", "F"))
        self.D.setText(_translate("MainWindow", "D"))
        self.Backsp.setText(_translate("MainWindow", "Backsp"))
        self.label.setText(_translate("MainWindow", "Из"))
        self.lineEdit.setText(_translate("MainWindow", "Введите число"))
        self.label_2.setText(_translate("MainWindow", "В"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
