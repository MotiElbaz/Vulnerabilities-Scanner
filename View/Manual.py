# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manual.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Objects.Subnet as Subnet
import Objects.Node as Node
import Objects.Reachability as Reachability
import re
import json


class Ui_Form(object):

    nodesName = []
    subnets = []
    nodes = []
    reachability = dict()
    vulens = []
    policy = ''
    rules = []
    rate = 0
    network = dict()
    UI = None

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
        self.nodesLayout = QtWidgets.QFormLayout()
        self.nodesLayout.setObjectName("nodesLayout")
        self.nameLabel_2 = QtWidgets.QLabel(Form)
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.nodesLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nameLabel_2)
        self.nameLineEdit_2 = QtWidgets.QLineEdit(Form)
        self.nameLineEdit_2.setObjectName("nameLineEdit_2")
        self.nodesLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit_2)
        self.labelLabel = QtWidgets.QLabel(Form)
        self.labelLabel.setObjectName("labelLabel")
        self.nodesLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelLabel)
        self.labelLineEdit = QtWidgets.QLineEdit(Form)
        self.labelLineEdit.setObjectName("labelLineEdit")
        self.nodesLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelLineEdit)
        self.descriptionLabel_2 = QtWidgets.QLabel(Form)
        self.descriptionLabel_2.setObjectName("descriptionLabel_2")
        self.nodesLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.descriptionLabel_2)
        self.descriptionLineEdit_2 = QtWidgets.QLineEdit(Form)
        self.descriptionLineEdit_2.setObjectName("descriptionLineEdit_2")
        self.nodesLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.descriptionLineEdit_2)
        self.vulnerabilitiesCVELabel = QtWidgets.QLabel(Form)
        self.vulnerabilitiesCVELabel.setObjectName("vulnerabilitiesCVELabel")
        self.nodesLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.vulnerabilitiesCVELabel)
        self.vulnerabilitiesCVELineEdit = QtWidgets.QLineEdit(Form)
        self.vulnerabilitiesCVELineEdit.setObjectName("vulnerabilitiesCVELineEdit")
        self.nodesLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.vulnerabilitiesCVELineEdit)
        self.vulnerabilitiesPortEdit = QtWidgets.QLineEdit(Form)
        self.vulnerabilitiesPortEdit.setObjectName("vulnerabilitiesPortEdit")
        self.vulnerabilitiesPortLabel = QtWidgets.QLabel(Form)
        self.vulnerabilitiesPortLabel.setObjectName("vulnerabilitiesPortLabel")
        self.nodesLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.vulnerabilitiesPortLabel)
        self.nodesLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.vulnerabilitiesPortEdit)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.nodesLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.nodesLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pushButton_3)
        self.nodesLabel = QtWidgets.QLabel(Form)
        self.nodesLabel.setObjectName("nodesLabel")
        self.nodesLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nodesLabel)
        self.horizontalLayout_2.addLayout(self.nodesLayout)
        self.reachLayout = QtWidgets.QFormLayout()
        self.reachLayout.setObjectName("reachLayout")
        self.reachLabel = QtWidgets.QLabel(Form)
        self.reachLabel.setObjectName("reachLabel")
        self.reachLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.reachLabel)
        self.defaultPolicyLabel = QtWidgets.QLabel(Form)
        self.defaultPolicyLabel.setObjectName("defaultPolicyLabel")
        self.reachLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.defaultPolicyLabel)
        self.defaultPolicyLineEdit = QtWidgets.QLineEdit(Form)
        self.defaultPolicyLineEdit.setObjectName("defaultPolicyLineEdit")
        self.reachLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.defaultPolicyLineEdit)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.reachLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton_4)
        self.sourceLabel_2 = QtWidgets.QLabel(Form)
        self.sourceLabel_2.setObjectName("sourceLabel_2")
        self.reachLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.sourceLabel_2)
        self.sourceComboBox = QtWidgets.QComboBox(Form)
        self.sourceComboBox.setObjectName("sourceComboBox")
        self.reachLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sourceComboBox)
        self.destinationLabel = QtWidgets.QLabel(Form)
        self.destinationLabel.setObjectName("destinationLabel")
        self.reachLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.destinationLabel)
        self.destinationComboBox = QtWidgets.QComboBox(Form)
        self.destinationComboBox.setObjectName("destinationComboBox")
        self.reachLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.destinationComboBox)
        self.portLabel = QtWidgets.QLabel(Form)
        self.portLabel.setObjectName("portLabel")
        self.reachLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.portLabel)
        self.portLineEdit = QtWidgets.QLineEdit(Form)
        self.portLineEdit.setObjectName("portLineEdit")
        self.reachLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.portLineEdit)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.reachLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pushButton_5)
        self.horizontalLayout_2.addLayout(self.reachLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.rateLayout = QtWidgets.QFormLayout()
        self.rateLayout.setObjectName("rateLayout")
        self.rateLineEdit = QtWidgets.QLineEdit(Form)
        self.rateLineEdit.setObjectName("rateLineEdit")
        self.rateLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rateLineEdit)
        self.rateLabel = QtWidgets.QLabel(Form)
        self.rateLabel.setObjectName("rateLabel")
        self.rateLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rateLabel)
        self.verticalLayout.addLayout(self.rateLayout)
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton.clicked.connect(self.addSubnet)
        self.pushButton_2.clicked.connect(self.addVulen)
        self.pushButton_3.clicked.connect(self.addNode)
        self.pushButton_4.clicked.connect(self.setPolicy)
        self.pushButton_5.clicked.connect(self.addRule)
        self.pushButton_6.clicked.connect(self.finishInsert)
        self.pushButton_7.clicked.connect(self.reset)

        self.sourceComboBox.addItems(self.nodesName)
        self.destinationComboBox.addItems(self.nodesName)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.network["subnets"] = []
        self.network["nodes"] = []
        self.reachability["defaultPolicy"] = ''
        self.reachability["rules"] = []
        self.network["reachability"] = dict()
        self.network["reachability"]["defaultPolicy"] = ''
        self.network["reachability"]["rules"] = []

    def reset(self):
        self.msgLabel.setText('')
        self.vulnerabilitiesPortEdit.setText('')
        self.destinationComboBox.clear()
        self.sourceComboBox.clear()
        self.nodesName = []
        self.subnets = []
        self.nodes = []
        self.reachability = dict()
        self.vulens = []
        self.policy = ''
        self.rules = []
        self.rate = 0
        self.network = dict()
        self.msgLabel.setText('')
        self.iDLineEdit.setText('')
        self.nameLineEdit.setText('')
        self.descriptionLineEdit.setText('')
        self.iPRangeLineEdit.setText('')
        self.vulnerabilitiesCVELineEdit.setText('')
        self.nameLineEdit_2.setText('')
        self.labelLineEdit.setText('')
        self.descriptionLineEdit_2.setText('')
        self.portLineEdit.setText('')
        self.defaultPolicyLineEdit.setText('')

    def finishInsert(self):
        msg = ''
        if len(self.nodes) == 0:
            msg = 'There is no nodes, please add node.'
            self.msgLabel.setText(msg)
            return
        if len(self.rules) == 0:
            msg = 'There is no rules, please add rule.'
            self.msgLabel.setText(msg)
            return
        if self.policy == '':
            msg = 'There is no policy, please add policy.'
            self.msgLabel.setText(msg)
            return
        if len(self.subnets) == 0:
            msg = 'There is no subnets, please add subnet.'
            self.msgLabel.setText(msg)
            return
        try:
            self.rate = int(self.rateLineEdit.text())
        except:
            self.rate = 0
        if self.rate > 10 or self.rate < 1:
            self.msgLabel.setText('Please enter Rate between 1-10.')
            return
        #self.network["subnets"] = self.subnets
        #self.network["nodes"] = self.nodes
        self.reachability["defaultPolicy"] = self.policy
        self.reachability["rules"] = self.rules
        #self.network["reachability"] = self.reachability
        self.msgLabel.setText('')
        myDict = {
            "subnets": self.subnets,
            "nodes": self.nodes,
            "reachability": self.reachability
        }
        for node in self.nodes:
            if node['name'].lower() == 'internet':
                js = json.dumps(myDict)
                self.UI.setManualResultsPage(js, self.rate, 'manual')
            else:
                self.msgLabel.setText('You need to add Internet node.')

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
        # subnet = Subnet.Subnet(id, name, desc, ip)
        subnet = {
            "id": id,
            "name": name,
            "desc": desc,
            "ipRange": ip
        }
        self.subnets.append(subnet)
        self.network['subnets'].append(subnet)

    def addVulen(self):
        cve = self.vulnerabilitiesCVELineEdit.text()
        ip = self.vulnerabilitiesPortEdit.text()
        try:
            ip = int(ip)
        except:
            self.msgLabel.setText("Please Enter Port Number.")
            return
        if ip < 0 or ip > 65535:
            self.msgLabel.setText("Please Port number between 0-65535.")
            return
        parts = cve.split('-')
        year = 0
        num = 0
        msg = 'Invalid CVE. Please Enter a valid CVE.'
        if len(parts) != 3:
            msg = 'Invalid CVE. Please Enter a valid CVE.'
        try:
            year = int(parts[1])
            num = int(parts[2])
        except:
            msg = 'Invalid CVE. Please Enter a valid CVE.'
        if parts[0] == 'CVE':
            if year > 1998 and year < 2020:
                if num >= 0:
                    self.vulens.append(cve)
                    msg = 'CVE added.'
                    self.vulnerabilitiesCVELineEdit.setText('')
        self.msgLabel.setText(msg)
        self.vulnerabilitiesPortEdit.setText('')

    def addNode(self):
        if len(self.vulens) == 0:
            msg = 'If there is no vulnerabilities in the host do not add him' \
                  ', if there is vulnerabilities, please add them.'
            self.msgLabel.setText(msg)
            return
        name = self.nameLineEdit_2.text()
        label = self.labelLineEdit.text()
        desc = self.descriptionLineEdit_2.text()
        if name == '' or label == '' or desc == '':
            self.msgLabel.setText('All fields required! Please Fill the missing fields.')
            return
        if name in self.nodesName:
            self.msgLabel.setText('Node already exists. Please enter new node.')
            return
        # node = Node.Node(name, label, desc, self.vulens)
        node = {
            "name": name,
            "label": label,
            "desc": desc,
            "vulnerabilities": self.vulens
        }
        self.vulens = []
        self.nodes.append(node)
        self.nodesName.append(name)
        self.sourceComboBox.addItem(name)
        self.destinationComboBox.addItem(name)
        self.msgLabel.setText('Node added.')
        self.nameLineEdit_2.setText('')
        self.labelLineEdit.setText('')
        self.descriptionLineEdit_2.setText('')

    def setPolicy(self):
        policy = self.defaultPolicyLineEdit.text()
        policy = policy.upper()
        msg = 'Please Enter Policy, Accept/Deny.'
        if policy == 'ACCEPT' or policy == 'DENY':
            self.policy = policy
            self.network['reachability']['defaultPolicy'] = policy
            msg = 'Policy added.'
        self.msgLabel.setText(msg)

    def addRule(self):
        source = self.sourceComboBox.currentText()
        dest = self.destinationComboBox.currentText()
        if source == '' or dest == '':
            self.msgLabel.setText('You need to chose source and target.')
            return
        port = self.portLineEdit.text()
        if port != '*':
            try:
                port = int(port)
            except:
                self.msgLabel.setText('Invalid port number, please enter port between 0-65535.')
                return
            if port < 0 or port > 65536:
                self.msgLabel.setText('Invalid port number, please enter port between 0-65535.')
                return
        if source == dest:
            self.msgLabel.setText('Source can not be the same as destination.')
            return
        for rule in self.rules:
            if source in rule['source']:
                if port in rule['ports']:
                    if dest not in rule['destination']:
                        rule['destination'].append(dest)
                        self.msgLabel.setText('Rule added.')
                        self.portLineEdit.setText('')
                        return
                    else:
                        self.msgLabel.setText('Rule already exists.')
                        return
        ruleDict = dict()
        sources = []
        sources.append(source)
        destinations = []
        destinations.append(dest)
        ports = []
        ports.append(str(port))
        ruleDict['source'] = sources
        ruleDict['destination'] = destinations
        ruleDict['ports'] = ports
        ruleDict['action'] = 'ACCEPT'
        self.msgLabel.setText('Rule added.')
        self.rules.append(ruleDict)
        self.network['reachability']['rules'].append(ruleDict)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.msgLabel.setText(_translate("Form", ""))
        self.iDLabel.setText(_translate("Form", "ID"))
        self.nameLabel.setText(_translate("Form", "Name"))
        self.descriptionLabel.setText(_translate("Form", "Description"))
        self.iPRangeLabel.setText(_translate("Form", "IP Range"))
        self.pushButton.setText(_translate("Form", "Add Subnet"))
        self.subnetsLabel.setText(_translate("Form", "Subnets"))
        self.nameLabel_2.setText(_translate("Form", "Name"))
        self.labelLabel.setText(_translate("Form", "Label"))
        self.descriptionLabel_2.setText(_translate("Form", "Description"))
        self.vulnerabilitiesCVELabel.setText(_translate("Form", "Vulnerability (CVE)"))
        self.vulnerabilitiesPortLabel.setText(_translate("Form", "Vulnerability Port"))
        self.pushButton_2.setText(_translate("Form", "Add Vulnerability"))
        self.pushButton_3.setText(_translate("Form", "Add Node"))
        self.nodesLabel.setText(_translate("Form", "Nodes"))
        self.reachLabel.setText(_translate("Form", "Reachbality"))
        self.defaultPolicyLabel.setText(_translate("Form", "Default Policy"))
        self.pushButton_4.setText(_translate("Form", "Set Policy"))
        self.sourceLabel_2.setText(_translate("Form", "Source"))
        self.destinationLabel.setText(_translate("Form", "Destination"))
        self.portLabel.setText(_translate("Form", "Port"))
        self.pushButton_5.setText(_translate("Form", "Add Rule"))
        self.rateLabel.setText(_translate("Form", "Rate"))
        self.pushButton_6.setText(_translate("Form", "Finish"))
        self.pushButton_7.setText(_translate("Form", "Reset"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
