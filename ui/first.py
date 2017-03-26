# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\first.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(497, 278)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 451, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.edt_file_one = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.edt_file_one.setObjectName("edt_file_one")
        self.horizontalLayout.addWidget(self.edt_file_one)
        self.btn_file_one = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_file_one.setObjectName("btn_file_one")
        self.horizontalLayout.addWidget(self.btn_file_one)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 120, 451, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.edt_file_two = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.edt_file_two.setObjectName("edt_file_two")
        self.horizontalLayout_2.addWidget(self.edt_file_two)
        self.btn_file_two = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_file_two.setObjectName("btn_file_two")
        self.horizontalLayout_2.addWidget(self.btn_file_two)
        self.btn_create = QtWidgets.QPushButton(self.centralwidget)
        self.btn_create.setGeometry(QtCore.QRect(390, 240, 75, 23))
        self.btn_create.setObjectName("btn_create")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "文件1"))
        self.btn_file_one.setText(_translate("MainWindow", "浏览"))
        self.label_2.setText(_translate("MainWindow", "文件2"))
        self.btn_file_two.setText(_translate("MainWindow", "浏览"))
        self.btn_create.setText(_translate("MainWindow", "生成excel"))

