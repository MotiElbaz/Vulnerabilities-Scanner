# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MENU.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):

    UI = None

    def setupUi(self, Menu, UI):
        self.UI = UI
        Menu.setObjectName("Menu")
        Menu.resize(300, 800)
        Menu.setStyleSheet("\n""background-color: rgb(31,40,51);")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Menu)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.name = QtWidgets.QLabel(Menu)
        self.name.setStyleSheet("color: rgb(255, 255, 255);\n""font: 25 20pt \"Arial\";")
        self.name.setObjectName("name")
        self.verticalLayout_3.addWidget(self.name, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line = QtWidgets.QFrame(Menu)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.auto_btn = QtWidgets.QPushButton(Menu)
        self.auto_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 25 20pt \"Arial\";\n""\n""")
        self.auto_btn.setObjectName("auto_btn")
        self.verticalLayout_3.addWidget(self.auto_btn)
        self.manual_btn = QtWidgets.QPushButton(Menu)
        self.manual_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 25 20pt \"Arial\";\n""")
        self.manual_btn.setObjectName("manual_btn")
        self.verticalLayout_3.addWidget(self.manual_btn)
        self.demo_btn = QtWidgets.QPushButton(Menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.demo_btn.sizePolicy().hasHeightForWidth())
        self.demo_btn.setSizePolicy(sizePolicy)
        self.demo_btn.setMaximumSize(QtCore.QSize(306, 16777215))
        self.demo_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 25 20pt \"Arial\";\n""")
        self.demo_btn.setObjectName("demo_btn")
        self.verticalLayout_3.addWidget(self.demo_btn)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(Menu)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(Menu)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(Menu)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.auto_btn.clicked.connect(self.autoBtnEvent)
        self.demo_btn.clicked.connect(self.demoBtnEvent)
        self.manual_btn.clicked.connect(self.manualBtnEvent)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def manualBtnEvent(self):
        self.UI.setManualPage('manual')

    def autoBtnEvent(self):
        self.UI.setAutoPage('auto')

    def demoBtnEvent(self):
        self.UI.setDemoPage('demo')

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Form"))
        self.name.setText(_translate("Menu", "Vulnerabilities Scanner"))
        self.auto_btn.setText(_translate("Menu", "Automatic Scan"))
        self.manual_btn.setText(_translate("Menu", "Manual Scan"))
        self.demo_btn.setText(_translate("Menu", "Demo"))

