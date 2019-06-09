import Model.VSModel as Model
import Model.DAL as DAL
import Utils.CVE_Data as CVE
import json
import Model.Scanner as Scanner
import Model.AlgorithmEngine as ae
import Controller.VSController as Controller
#import View.UI as UI
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import View.UI as UI


if __name__ == "__main__":
    # dal = DAL.DAL()
    # dal.downloadNVD()
    model = Model.VSModel()
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = UI.Ui_UI()
    controller = Controller.VSController(model, ui)
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

    # Some testing -------------------------------------------------------------
    # dal = DAL.DAL()
    # model.setDB()
    # model.demo()
    # model.getShortPath('Public Database Server')
    # model.getVulnerablePath('Public Database Server')
    # model.getExposeComponent()
    # scanner = Scanner.Scanner()
    # network = scanner.scan([])
    # ae = ae.AlgorithmEngine()
    # ae.generateAttackGraph(network)
    # model.auto()
    # js = {"subnets": [{"id": "Internet", "name": "Internet", "desc": "Internet", "ipRange": "0.0.0.0"}], "nodes": [{"name": "Internet", "label": "Internet", "desc": "Attacker's location", "vulnerabilities": ["CVE-1999-00"]}, {"name": "Apache HTTP Server", "label": "Apache HTTP Server", "desc": "Apache HTTP Server", "vulnerabilities": ["CVE-2006-3747"]}, {"name": "REDHAT", "label": "REDHAT", "desc": "REDHAT", "vulnerabilities": ["CVE-2014-8174"]}, {"name": "Cisco Router", "label": "Cisco Router", "desc": "Cisco Router", "vulnerabilities": ["CVE-2017-3882"]}, {"name": "Host Machine(Linux)", "label": "Host Machine(Linux)", "desc": "Host Machine(Linux)", "vulnerabilities": ["CVE-2003-1604"]}, {"name": "Guest Machine", "label": "Guest Machine", "desc": "Guest Machine", "vulnerabilities": ["CVE-2008-2098"]}], "reachability": {"defaultPolicy": "DENY", "rules": [{"source": ["Internet"], "destination": ["Apache HTTP Server"], "ports": ["80"], "action": "ACCEPT"}, {"source": ["Internet"], "destination": ["Host Machine(Linux)"], "ports": ["80"], "action": "ACCEPT"}, {"source": ["Apache HTTP Server"], "destination": ["REDHAT"], "ports": ["80"], "action": "ACCEPT"}, {"source": ["Apache HTTP Server"], "destination": ["Cisco Router"], "ports": ["80"], "action": "ACCEPT"}, {"source": ["Host Machine(Linux)"], "destination": ["Guest Machine"], "ports": ["80"], "action": "ACCEPT"}, {"source": ["Host Machine(Linux)"], "destination": ["Internet"], "ports": ["80"], "action": "ACCEPT"}, {"source": ["Host Machine(Linux)"], "destination": ["Cisco Router"], "ports": ["80"], "action": "ACCEPT"}, {"source": ["Guest Machine"], "destination": ["Host Machine(Linux)"], "ports": ["80"], "action": "ACCEPT"}, {"source": ["Cisco Router"], "destination": ["Apache HTTP Server"], "ports": ["80"], "action": "ACCEPT"}, {"source": ["Cisco Router"], "destination": ["REDHAT"], "ports": ["80"], "action": "ACCEPT"}, {"source": ["Cisco Router"], "destination": ["Host Machine(Linux)"], "ports": ["80"], "action": "ACCEPT"}]}}
    # js_str = json.dumps(js)
    # model.manual(js_str)
    # network = model.network
    # node = network['nodes'][2]
    # print(node)
    # model.getShortPath(node)
    # model.getVulnerablePath(node)
    # model.getExposeComponent()
    # dal = DAL.DAL()
    # dal.createDB()
