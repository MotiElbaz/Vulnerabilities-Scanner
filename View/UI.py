# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox
import sys
import View.Menu as Menu
import View.Results as Results
import View.Auto as Auto
import View.Manual as Manual
import View.Main as Main
import json
import traceback


class Ui_UI(object):

    currPage = None
    listeners = set()
    subnets = None
    networkDemo = None
    networkManual = None
    networkAuto = None
    demoFinished = False
    manualFinished = False
    autoFinished = False
    answer = ''
    userRate = 0

    def setupUi(self, UI):
        UI.setObjectName("UI")
        UI.resize(1200, 800)
        UI.setStyleSheet("background-color: rgb(102,252,241);")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(UI)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.menu_widget = QtWidgets.QWidget()
        self.Menu = Menu.Ui_Menu()
        self.Menu.setupUi(self.menu_widget, self)
        self.menu_widget.show()
        self.horizontalLayout_2.addWidget(self.menu_widget)

        self.main = QtWidgets.QWidget()
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setSpacing(10)
        self.main.setLayout(self.mainLayout)

        self.welcomeLabel = QtWidgets.QLabel()
        self.welcomeLabel.setText('Welcome to Vulnerability Scanner')
        self.main.show()
        self.mainLayout.addWidget(self.main)

        self.horizontalLayout_2.addWidget(self.main)
        self.currPage = self.main

        #self.results_widget = QtWidgets.QWidget()
        #self.results = Results.Ui_Form()
        #self.results.setupUi(self.results_widget)
        #self.results_widget.show()
        #self.horizontalLayout_2.addWidget(self.results_widget)

        self.auto_results_widget = QtWidgets.QWidget()
        self.auto_results = Results.Ui_Form()
        self.auto_results.setupUi(self.auto_results_widget, 'auto', self)
        self.horizontalLayout_2.addWidget(self.auto_results_widget)
        self.auto_results_widget.hide()
        #self.results_widget.show()

        self.manual_results_widget = QtWidgets.QWidget()
        self.manual_results = Results.Ui_Form()
        self.manual_results.setupUi(self.manual_results_widget, 'manual', self)
        self.horizontalLayout_2.addWidget(self.manual_results_widget)
        self.manual_results_widget.hide()

        self.auto_widget = QtWidgets.QWidget()
        self.auto = Auto.Ui_Form()
        self.auto.setupUi(self.auto_widget, self)
        self.horizontalLayout_2.addWidget(self.auto_widget)
        self.auto_widget.hide()

        self.manual_widget = QtWidgets.QWidget()
        self.manual = Manual.Ui_Form()
        self.manual.setupUi(self.manual_widget, self)
        self.horizontalLayout_2.addWidget(self.manual_widget)
        self.manual_widget.hide()

        self.main_widget = QtWidgets.QWidget()
        self.main = Main.Ui_Form()
        self.main.setupUi(self.main_widget)
        self.horizontalLayout_2.addWidget(self.main_widget)
        self.currPage = self.main_widget
        self.main_widget.show()

        self.demo_widget = QtWidgets.QWidget()
        self.demo = Results.Ui_Form()
        self.demo.setupUi(self.demo_widget, 'demo', self)
        self.horizontalLayout_2.addWidget(self.demo_widget)
        self.demo_widget.hide()
        #self.demo_widget.show()

        self.retranslateUi(UI)
        QtCore.QMetaObject.connectSlotsByName(UI)

        self.fireDBEvent()

    def retranslateUi(self, UI):
        _translate = QtCore.QCoreApplication.translate
        UI.setWindowTitle(_translate("UI", "VS"))

    def setAutoPage(self, type=''):
        if self.currPage is not None:
            self.currPage.hide()
        if self.autoFinished is True:
            self.currPage = self.auto_results_widget
        else:
            self.currPage = self.auto_widget
        self.currPage.show()

    def setManualPage(self, type=''):
        if self.currPage is not None:
            self.currPage.hide()
        if self.manualFinished is True:
            self.currPage = self.manual_results_widget
        else:
            self.currPage = self.manual_widget
        self.currPage.show()

    def setDemoPage(self, type=''):
        if self.currPage is not None:
            self.currPage.hide()
        if self.demoFinished is False:
            self.fireDemoEvent()
        if self.currPage == self.demo_widget:
            return
        self.currPage = self.demo_widget
        self.currPage.show()

    def manualFromModel(self, rate, network):
        self.manualFinished = True
        if self.currPage is not None:
            self.currPage.hide()
        if self.currPage == self.manual_results_widget:
            return
        self.manual_results.setRate(rate, self.userRate)
        self.manual_results.setGraph(network)
        self.networkManual = network
        self.currPage = self.manual_results_widget
        self.currPage.show()

    def autoFromModel(self, rate, network, answer):
        if answer != 'Scan done.':
            self.showdialog(answer)
            return
        self.autoFinished = True
        if self.currPage is not None:
            self.currPage.hide()
        if self.currPage == self.auto_results_widget:
            return
        self.auto_results.setRate(rate, self.userRate)
        self.auto_results.setGraph(network)
        self.networkAuto = network
        self.currPage = self.auto_results_widget
        self.currPage.show()

    def demoFromModel(self, rate, network):
        self.demoFinished = True
        if self.currPage is not None:
            self.currPage.hide()
        if self.currPage == self.demo_widget:
            return
        self.demo.setRate(rate, self.userRate)
        self.demo.setGraph(network)
        self.networkDemo = network
        self.currPage = self.demo_widget
        self.currPage.show()

    def shortPathFromModel(self, answer):
        if answer != '':
            self.showdialog(answer)
            if self.currPage == self.demo_widget and self.networkDemo is not None:
                self.demo.msgLabel.setText(answer)
                return
            if self.currPage == self.manual_widget and self.networkManual is not None:
                self.manual_results.msgLabel.setText(answer)
                return
            if self.currPage == self.auto_widget and self.net:
                self.auto_results.msgLabel.setText(answer)
                return
            return
        if self.currPage == self.demo_widget and self.networkDemo is not None:
            self.demo.shortPath()
            return
        if self.currPage == self.manual_widget and self.networkManual is not None:
            self.manual_results.shortPath()
            return
        if self.currPage == self.auto_widget and self.net:
            self.auto_results.shortPath()
            return

    def vulnerablePathFromModel(self, answer):
        if answer != '':
            self.showdialog(answer)
            return
        if self.currPage == self.demo_widget:
            self.demo.vulnerablePath()
            return
        if self.currPage == self.manual_widget:
            self.manual_results.vulnerablePath()
            return
        if self.currPage == self.auto_widget:
            self.auto_results.vulnerablePath()
            return

    def exposeComponentFromModel(self, answer):
        if answer != '':
            self.showdialog(answer)
            return
        if self.currPage == self.demo_widget:
            self.demo.exposeComponent()
            return
        if self.currPage == self.manual_widget:
            self.manual_results.exposeComponent()
            return
        if self.currPage == self.auto_widget:
            self.auto_results.exposeComponent()
            return

    def setAutoResultsPage(self, subnets, userRate, type=''):
        self.subnets = subnets
        if self.currPage is not None:
            self.currPage.hide()
        if self.autoFinished is False:
            self.fireAutoEvent(subnets)
        self.currPage = self.auto_results_widget
        self.userRate = userRate
        # self.currPage.show()

    def setManualResultsPage(self, networkManual, userRate, type=''):
        self.networkManual = networkManual
        if self.currPage is not None:
            self.currPage.hide()
        if self.manualFinished is False:
            self.fireManualEvent(networkManual)
        self.currPage = self.manual_results_widget
        self.userRate = userRate
        self.currPage.show()

    def firePathsEvent(self, target):
        for listener in self.listeners:
            listener.shortPathFromUI(target)
            listener.vulnerablePathFromUI(target)
            listener.exposeComponentFromUI()

    def fireAutoEvent(self, subnets):
        for listener in self.listeners:
            listener.automaticFromUI(subnets)

    def fireManualEvent(self, network):
        for listener in self.listeners:
            listener.manualFromUI(network)

    def fireDemoEvent(self):
        for listener in self.listeners:
            listener.demoFromUI()

    def fireDBEvent(self):
        for listener in self.listeners:
            listener.setDBFromUI()

    def register(self, listener):
        self.listeners.add(listener)

    def setDB(self, answer):
        self.answer = answer
        if answer == '':
            # msg.setIcon(QMessageBox.Information)
            answer = 'DB is ready to go.'
        self.showdialog(answer)

    def showdialog(self, answer):
        msg = QMessageBox()
        QMessageBox.about(msg, 'VS', answer)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_UI()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
