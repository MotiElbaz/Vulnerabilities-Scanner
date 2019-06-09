# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 800)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.msgLabel = QtWidgets.QLabel(Form)
        self.msgLabel.setObjectName("msgLabel")
        self.verticalLayout_2.addWidget(self.msgLabel, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.msgLabel.setText(_translate("Form", "Welcome to Vulnerability Scanner "))
#         self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Open Sans,Arial,sans-serif\'; font-size:14px; color:#000000; background-color:#ffffff;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse lobortis vitae turpis et commodo. Suspendisse potenti. Quisque ut nulla ultricies felis porttitor convallis at et urna. Aenean cursus et justo et volutpat. Praesent interdum lectus id tortor finibus, sed laoreet eros aliquam. Ut maximus consectetur consequat. Suspendisse suscipit est non blandit volutpat. Sed felis tortor, vehicula in eros a, pulvinar aliquet risus. Vestibulum consectetur velit elit, vel sagittis urna commodo sit amet. Fusce vel sem a ligula laoreet semper a non nunc. Nunc convallis tortor nec ultricies ultricies. Ut bibendum urna mi, quis finibus felis faucibus in. Integer non purus sit amet justo gravida tincidunt.</span></p>\n"
# "<p style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Open Sans,Arial,sans-serif\'; font-size:14px; color:#000000; background-color:#ffffff;\">Etiam ante elit, mattis id ipsum nec, aliquam dignissim sapien. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Suspendisse potenti. Duis eu urna id urna facilisis efficitur. Cras facilisis pellentesque elementum. Aliquam elementum, nibh a tincidunt sodales, erat turpis elementum nisl, vitae posuere erat ligula a tellus. Maecenas ut efficitur enim. Aenean vitae ullamcorper neque.</span></p></body></html>"))

#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     widget = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(widget)
#     widget.show()
#     sys.exit(app.exec_())
