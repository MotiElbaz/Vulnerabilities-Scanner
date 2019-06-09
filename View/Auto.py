# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auto.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import re
import Objects.Subnet as Subnet
import json


class Ui_Form(object):

    subnets = []
    UI = None
    rate = 0

    def setupUi(self, Form, UI):
        self.UI = UI
        Form.setObjectName("Form")
        Form.resize(900, 800)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.msgLabel = QtWidgets.QLabel(Form)
        self.msgLabel.setObjectName("msgLabel")
        self.verticalLayout.addWidget(self.msgLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.subnetsLayout = QtWidgets.QFormLayout()
        self.subnetsLayout.setObjectName("subnetsLayout")

        self.iDLabel = QtWidgets.QLabel(Form)
        self.iDLabel.setObjectName("iDLabel")
        self.subnetsLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.iDLabel)

        self.iDLineEdit = QtWidgets.QLineEdit(Form)
        self.iDLineEdit.setObjectName("iDLineEdit")
        self.subnetsLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.iDLineEdit)

        self.nameLabel = QtWidgets.QLabel(Form)
        self.nameLabel.setObjectName("nameLabel")
        self.subnetsLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QtWidgets.QLineEdit(Form)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.subnetsLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)

        self.descriptionLabel = QtWidgets.QLabel(Form)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.subnetsLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.descriptionLabel)

        self.descriptionLineEdit = QtWidgets.QLineEdit(Form)
        self.descriptionLineEdit.setObjectName("descriptionLineEdit")
        self.subnetsLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.descriptionLineEdit)

        self.iPRangeLabel = QtWidgets.QLabel(Form)
        self.iPRangeLabel.setObjectName("iPRangeLabel")
        self.subnetsLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.iPRangeLabel)

        self.iPRangeLineEdit = QtWidgets.QLineEdit(Form)
        self.iPRangeLineEdit.setObjectName("iPRangeLineEdit")
        self.subnetsLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.iPRangeLineEdit)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.subnetsLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pushButton)

        self.subnetsLabel = QtWidgets.QLabel(Form)
        self.subnetsLabel.setObjectName("subnetsLabel")
        self.subnetsLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.subnetsLabel)

        self.horizontalLayout_2.addLayout(self.subnetsLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)

        self.rateLabel = QtWidgets.QLabel(Form)
        self.rateLabel.setObjectName("rateLabel")
        self.subnetsLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.rateLabel)

        self.rateLineEdit = QtWidgets.QLineEdit(Form)
        self.rateLineEdit.setObjectName("rateLineEdit")
        self.subnetsLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.rateLineEdit)

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setObjectName("pushButton_7")
        self.subnetsLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.pushButton_7)

        # self.rateBtn = QtWidgets.QPushButton(Form)
        # self.rateBtn.setObjectName("rateBtn")
        # self.subnetsLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.rateBtn)

        self.pushButton.clicked.connect(self.addSubnet)
        self.pushButton_6.clicked.connect(self.finishSubnets)
        self.pushButton_7.clicked.connect(self.reset)
        # self.rateBtn.clicked.connect(self.rateEvent)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def reset(self):
        self.subnets = []
        self.rate = 0
        self.msgLabel.setText('')
        self.rateLineEdit.setText('')
        self.iDLineEdit.setText('')
        self.iPRangeLineEdit.setText('')
        self.nameLineEdit.setText('')
        self.descriptionLineEdit.setText('')


    def addSubnet(self):
        id = self.iDLineEdit.text()
        name = self.nameLineEdit.text()
        desc = self.descriptionLineEdit.text()
        ip = self.iPRangeLineEdit.text()
        if id is '' or name is '' or desc is '' or ip is '':
            self.msgLabel.setText('All fields required! Please Fill the missing fields.')
            return
        self.msgLabel.setText('')
        subnetReg = re.findall("^([0-9]{1,3}\.){3}[0-9]{1,3}(\/24)?$", ip)
        if len(subnetReg) == 0:
            self.msgLabel.setText('Subnet IP Range is not valid, please valid range like this : 127.0.0.1/24 .')
            return
        self.msgLabel.setText('Subnet added.')
        self.iDLineEdit.setText('')
        self.nameLineEdit.setText('')
        self.descriptionLineEdit.setText('')
        self.iPRangeLineEdit.setText('')
        subnet = Subnet.Subnet(id, name, desc, ip)
        self.subnets.append(subnet)

    def finishSubnets(self):
        if len(self.subnets) == 0:
            self.msgLabel.setText('No subnets added. Please add at least one subnet.')
            return
        try:
            self.rate = int(self.rateLineEdit.text())
        except:
            self.rate = 0
        if self.rate > 10 or self.rate < 1:
            self.msgLabel.setText('Please enter Rate between 1-10.')
            return
        self.msgLabel.setText('')
        self.UI.setAutoResultsPage(self.subnets, self.rate, 'auto')

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.msgLabel.setText(_translate("Form", ""))
        self.iDLabel.setText(_translate("Form", "ID"))
        self.nameLabel.setText(_translate("Form", "Name"))
        self.descriptionLabel.setText(_translate("Form", "Description"))
        self.iPRangeLabel.setText(_translate("Form", "IP Range"))
        self.pushButton.setText(_translate("Form", "Enter Subnet"))
        self.subnetsLabel.setText(_translate("Form", "Subnets"))
        self.rateLabel.setText(_translate("Form", "Rate"))
        # self.rateBtn.setText(_translate("Form", "Enter Rate"))
        self.pushButton_6.setText(_translate("Form", "Start Scan"))
        self.pushButton_7.setText(_translate("Form", "Reset"))
