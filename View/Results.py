# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class Ui_Form(object):

    UI = None
    rate = 0
    network = None

    def setupUi(self, Form, type, UI):
        self.scanover = True
        self.type = type
        self.UI = UI

        Form.setObjectName("Form")
        Form.resize(900, 800)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.fromLayout = QtWidgets.QHBoxLayout()
        self.fromLayout.setObjectName("fromLayout")
        self.targetNodeLabel = QtWidgets.QLabel(Form)
        self.targetNodeLabel.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "font: 25 12pt \"Arial\";\n"
                                           "")
        self.targetNodeLabel.setObjectName("targetNodeLabel")
        self.fromLayout.addWidget(self.targetNodeLabel)
        self.targetNodeLineEdit = QtWidgets.QLineEdit(Form)
        self.targetNodeLineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
                                              "font: 25 12pt \"Arial\";\n"
                                              "border: 1px solid grey;\n"
                                              "border-radius: 12px;\n"
                                              "padding 0 8px;\n"
                                              "selection-background-color: white;")
        self.targetNodeLineEdit.setObjectName("targetNodeLineEdit")
        self.fromLayout.addWidget(self.targetNodeLineEdit)
        self.pathBtn = QtWidgets.QPushButton(Form)
        self.pathBtn.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 25 12pt \"Arial\";")
        self.pathBtn.setObjectName("pathBtn")
        self.fromLayout.addWidget(self.pathBtn)
        self.mainLayout.addLayout(self.fromLayout)
        self.rateAnswerLabel = QtWidgets.QLabel(Form)
        self.rateAnswerLabel.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "font: 25 12pt \"Arial\";\n"
                                           "")
        self.rateAnswerLabel.setObjectName("rateAnswerLabel")
        self.mainLayout.addWidget(self.rateAnswerLabel)

        self.msgLabel = QtWidgets.QLabel(Form)
        self.msgLabel.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "font: 25 12pt \"Arial\";\n"
                                           "")
        self.msgLabel.setObjectName("msgLabel")
        self.mainLayout.addWidget(self.msgLabel)

        self.imgs = QtWidgets.QTabWidget(Form)
        self.imgs.setObjectName("imgs")

        self.graph = QtWidgets.QWidget()
        self.graph.setObjectName("graph")
        # self.graph_img = QtWidgets.QLabel(Form)
        # self.graph_map = QPixmap('..//Images//graph.png')
        # self.graph_img.setPixmap(self.graph_map)
        # self.graph.layout = QVBoxLayout(Form)
        # self.graph.layout.addWidget(self.graph_img)
        # self.graph.setLayout(self.graph.layout)
        self.imgs.addTab(self.graph, "")

        self.short_2 = QtWidgets.QWidget()
        self.short_2.setObjectName("short_2")
        self.short_img = QtWidgets.QLabel(Form)
        # self.short_map = QPixmap('..//Images//short.png')
        # self.short_img.setPixmap(self.short_map)
        self.short_2.layout = QVBoxLayout(Form)
        self.short_2.layout.addWidget(self.short_img)
        self.short_2.setLayout(self.short_2.layout)
        self.imgs.addTab(self.short_2, "")

        self.vulen = QtWidgets.QWidget()
        self.vulen.setObjectName("vulen")
        self.vulen_img = QtWidgets.QLabel(Form)
        # self.vulen_map = QPixmap('..//Images//vule.png')
        # self.vulen_img.setPixmap(self.vulen_map)
        self.vulen.layout = QVBoxLayout(Form)
        self.vulen.layout.addWidget(self.vulen_img)
        self.vulen.setLayout(self.vulen.layout)
        self.imgs.addTab(self.vulen, "")

        self.expose = QtWidgets.QWidget()
        self.expose.setObjectName("expose")
        self.expose_img = QtWidgets.QLabel(Form)
        # self.expose_map = QPixmap('..//Images//expose.png')
        # self.expose_img.setPixmap(self.expose_map)
        self.expose.layout = QVBoxLayout(Form)
        self.expose.layout.addWidget(self.expose_img)
        self.expose.setLayout(self.expose.layout)
        self.imgs.addTab(self.expose, "")

        self.mainLayout.addWidget(self.imgs)
        self.verticalLayout.addLayout(self.mainLayout)

        self.pathBtn.clicked.connect(self.nodeEvent)

        self.retranslateUi(Form)
        self.imgs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def nodeEvent(self):
        target = self.targetNodeLineEdit.text()
        for node in self.network['nodes']:
            if node.label.lower() == target.lower() or node.name.lower() == target.lower():
                self.msgLabel.setText('Searching for paths.')
                self.UI.firePathsEvent(node)
                return
        self.msgLabel.setText('Node is not found, Please enter a correct name.')

    def setGraph(self, network):
        self.graph_img = QtWidgets.QLabel()
        self.graph_map = QPixmap('Images//graph.png')
        self.graph_img.setPixmap(self.graph_map)
        self.graph.layout = QVBoxLayout()
        self.graph.layout.addWidget(self.graph_img)
        self.graph.setLayout(self.graph.layout)
        self.network = network

    def vulnerablePath(self):
        self.msgLabel.setText('Paths found.')
        # self.vulen_img = QtWidgets.QLabel()
        self.vulen_map = QPixmap('Images//vule.png')
        self.vulen_img.setPixmap(self.vulen_map)
        # self.vulen.layout = QVBoxLayout()
        # self.vulen.layout.addWidget(self.vulen_img)
        # self.vulen.setLayout(self.vulen.layout)

    def shortPath(self):
        # self.short_img = QtWidgets.QLabel()
        self.short_map = QPixmap('Images//short.png')
        self.short_img.setPixmap(self.short_map)
        # self.short_2.layout = QVBoxLayout()
        # self.short_2.layout.addWidget(self.short_img)
        # self.short_2.setLayout(self.short_2.layout)

    def exposeComponent(self):
        # self.expose_img = QtWidgets.QLabel()
        self.expose_map = QPixmap('Images//expose.png')
        self.expose_img.setPixmap(self.expose_map)
        # self.expose.layout = QVBoxLayout()
        # self.expose.layout.addWidget(self.expose_img)
        # self.expose.setLayout(self.expose.layout)

    def setRate(self, rate, userRate):
        self.rate = rate
        if rate <= userRate:
            self.rateAnswerLabel.setText("Rate is : " + str(self.rate) + " and system is secure.")
        else:
            self.rateAnswerLabel.setText("Rate is : " + str(self.rate) + " and system is not secure.")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.targetNodeLabel.setText(_translate("Form", "Target Node"))
        self.pathBtn.setText(_translate("Form", "Set Node"))
        self.rateAnswerLabel.setText(_translate("Form", "Rate is : "))
        self.msgLabel.setText(_translate("Form", ""))
        self.imgs.setTabText(self.imgs.indexOf(self.graph), _translate("Form", "Graph"))
        self.imgs.setTabText(self.imgs.indexOf(self.short_2), _translate("Form", "Shortest Path"))
        self.imgs.setTabText(self.imgs.indexOf(self.vulen), _translate("Form", "Vulnerable Path"))
        self.imgs.setTabText(self.imgs.indexOf(self.expose), _translate("Form", "Expose Component"))
