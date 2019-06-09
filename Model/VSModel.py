from Model.Scanner import Scanner
from Model.Interpreter import Interpreter
from Model.AlgorithmEngine import AlgorithmEngine
from Model.AnalysisEngine import AnalysisEngine
from Model.DAL import DAL
from threading import Lock
import json
import logging

logging.basicConfig(filename='LOG.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class VSModel:
    _instance = None
    scanner = Scanner()
    interpreter = Interpreter()
    algorithm = AlgorithmEngine()
    analysis = AnalysisEngine()
    dal = DAL()
    listeners = set()
    graph = None
    network = None
    rate = 0

    def __int__(self):
        self.scanner = Scanner()
        self.interpreter = Interpreter()
        self.algorithm = AlgorithmEngine()
        self.analysis = AnalysisEngine()
        self.dal = DAL()
        self.listeners = set()

    def auto(self, subnets):
        answer = 'Scan done.'
        try:
            self.network = self.scanner.scan(subnets)
            self.generateGraph()
        except:
            answer = 'Error while scanning lan topology, please download NMAP Binary files.'
            logging.info(answer.format())
            # self.fireAutomaticEvent(answer)
        self.fireAutomaticEvent(answer)

    def manual(self, network_json):
        logging.info('Start Interpret Network Details  ...'.format())
        self.network = self.interpreter.generateNetworkManual(network_json)
        # for key, li in self.network.items():
        #     print(key, "=>")
        #     for val in li:
        #         print(val)
        logging.info('Finish Interpret Network Details  ...'.format())
        self.generateGraph(False)
        self.fireManualEvent()

    def demo(self):
        demo = {
            "subnets": [
                {
                    "id": "internet",
                    "name": "Internet",
                    "desc": "Outside network",
                    "zone": "zone0",
                    "ipRange": "200.40.47.120/29"
                },
                {
                    "id": "sn1",
                    "name": "DMZ",
                    "desc": "Demilitarized zone",
                    "zone": "zone1",
                    "ipRange": "192.168.1.0/24"
                },
                {
                    "id": "sn2",
                    "name": "lan1",
                    "desc": "Internal network",
                    "zone": "zone2",
                    "ipRange": "192.168.17.0/24"
                }
            ],
            "nodes": [
                {
                    "id": "inet",
                    "name": "Internet",
                    "label": "Internet",
                    "desc": "Attacker's location",
                    "roles": ["Internet"],
                    "group": 0,
                    "locations": [
                        {"ip": "200.40.47.121", "subnetId": "internet"}
                    ],
                    "vulnerabilities": []
                },
                {
                    "id": "fw1",
                    "name": "fw1",
                    "label": "srx-3600-1",
                    "desc": "Main firewall",
                    "roles": ["Firewall", "Router", "ReachabilityControlPoint"],
                    "attributes": {"platform": "juniper"},
                    "group": 21,
                    "locations": [
                        {"ip": "200.40.47.122", "subnetId": "internet"},
                        {"ip": "192.168.1.1", "subnetId": "sn1"},
                        {"ip": "192.168.17.1", "subnetId": "sn2"}
                    ],
                    "vulnerabilities": [
                        {"id": "3", "score": "6.8", "ports": ["22"]}
                    ]
                },
                {
                    "id": "ws1_dmz",
                    "name": "web-server",
                    "label": "web-server (DMZ)",
                    "desc": "Public Web Server",
                    "roles": ["ExternalServer"],
                    "attributes": {"platform": "linux"},
                    "group": 1,
                    "locations": [
                        {"ip": "192.168.1.50", "subnetId": "sn1"}
                    ],
                    "vulnerabilities": [
                        {"id": "1", "score": "7.3", "ports": ["80", "8080"]},
                        {"id": "2", "score": "9.5", "ports": ["80", "8080"]},
                        {"id": "3", "score": "6.8", "ports": ["22"]}
                    ]
                },
                {
                    "id": "db1_dmz",
                    "name": "db-server",
                    "label": "db-server (DMZ)",
                    "desc": "Public Database Server",
                    "roles": ["ExternalServer"],
                    "attributes": {"platform": "linux"},
                    "group": 1,
                    "locations": [
                        {"ip": "192.168.1.75", "subnetId": "sn1"}
                    ],
                    "vulnerabilities": [
                        {"id": "3", "score": "6.8", "ports": ["22"]}
                    ]
                },
                {
                    "id": "mail1_dmz",
                    "name": "mail-server",
                    "label": "mail-server (DMZ)",
                    "desc": "Public SMTP Server",
                    "roles": ["ExternalServer"],
                    "attributes": {"platform": "linux"},
                    "group": 1,
                    "locations": [
                        {"ip": "192.168.1.90", "subnetId": "sn1"}
                    ],
                    "vulnerabilities": [
                        {"id": "3", "score": "6.8", "ports": ["22"]}
                    ]
                },
                {
                    "id": "sysadmin1",
                    "name": "sysadmin",
                    "label": "sysadmin host",
                    "desc": "Administration host",
                    "roles": ["AdministrationHost"],
                    "attributes": {"platform": "macos"},
                    "group": 2,
                    "locations": [
                        {"ip": "192.168.17.5", "subnetId": "sn2"}
                    ],
                    "vulnerabilities": [
                        {"id": "3", "score": "6.8", "ports": ["22"]}
                    ]
                },
                {
                    "id": "testing1",
                    "name": "testing-server",
                    "label": "testing-server (LAN)",
                    "desc": "Internal testing server",
                    "roles": ["InternalServer"],
                    "attributes": {"platform": "linux"},
                    "group": 2,
                    "locations": [
                        {"ip": "192.168.17.20", "subnetId": "sn2"}
                    ],
                    "vulnerabilities": [
                        {"id": "3", "score": "6.8", "ports": ["22"]}
                    ]
                },
                {
                    "id": "ws1_internal",
                    "name": "internal-web-server",
                    "label": "web-server (LAN)",
                    "desc": "Internal Web Server",
                    "roles": ["InternalServer"],
                    "attributes": {"platform": "linux"},
                    "group": 2,
                    "locations": [
                        {"ip": "192.168.17.35", "subnetId": "sn2"}
                    ],
                    "vulnerabilities": [
                        {"id": "1", "score": "7.3", "ports": ["80", "8080"]},
                        {"id": "2", "score": "9.5", "ports": ["80", "8080"]},
                        {"id": "3", "score": "6.8", "ports": ["22"]},
                        {"id": "4", "score": "9.3", "ports": ["0"]}
                    ]
                },
                {
                    "id": "win1",
                    "name": "win1-workstation",
                    "label": "win1-workstation (LAN)",
                    "desc": "Windows Workstation 1",
                    "roles": ["SingleHost"],
                    "attributes": {"platform": "windows"},
                    "group": 2,
                    "locations": [
                        {"ip": "192.168.17.51", "subnetId": "sn2"}
                    ],
                    "vulnerabilities": [
                        {"id": "5", "score": "8.3", "ports": [445]}
                    ]
                },
                {
                    "id": "win2",
                    "name": "win2-workstation",
                    "label": "win2-workstation (LAN)",
                    "desc": "Windows Workstation 2",
                    "roles": ["SingleHost"],
                    "attributes": {"platform": "windows"},
                    "group": 2,
                    "locations": [
                        {"ip": "192.168.17.52", "subnetId": "sn2"}
                    ],
                    "vulnerabilities": [
                        {"id": "5", "score": "8.3", "ports": [445]}
                    ]
                },
                {
                    "id": "win3",
                    "name": "win3-workstation",
                    "label": "win3-workstation (LAN)",
                    "desc": "Windows Workstation 3",
                    "roles": ["SingleHost"],
                    "attributes": {"platform": "windows"},
                    "group": 2,
                    "locations": [
                        {"ip": "192.168.17.53", "subnetId": "sn2"}
                    ],
                    "vulnerabilities": [
                        {"id": "5", "score": "8.3", "ports": [445]}
                    ]
                },
                {
                    "id": "linux1",
                    "name": "linux1-workstation",
                    "label": "linux1-workstation",
                    "desc": "Linux Workstation 1",
                    "roles": ["SingleHost"],
                    "attributes": {"platform": "linux"},
                    "group": 2,
                    "locations": [
                        {"ip": "192.168.17.81", "subnetId": "sn2"}
                    ],
                    "vulnerabilities": [
                        {"id": "3", "score": "6.8", "ports": ["22"]}
                    ]
                },
                {
                    "id": "linux2",
                    "name": "linux2-workstation",
                    "label": "linux2-workstation (LAN)",
                    "desc": "Linux Workstation 2",
                    "roles": ["SingleHost"],
                    "attributes": {"platform": "linux"},
                    "group": 2,
                    "locations": [
                        {"ip": "192.168.17.82", "subnetId": "sn2"}
                    ],
                    "vulnerabilities": [
                        {"id": "3", "score": "6.8", "ports": ["22"]}
                    ]
                },
                {
                    "id": "linux3",
                    "name": "linux3-workstation",
                    "label": "linux3-workstation (LAN)",
                    "desc": "Linux Workstation 3",
                    "roles": ["SingleHost"],
                    "attributes": {"platform": "linux"},
                    "group": 2,
                    "locations": [
                        {"ip": "192.168.17.83", "subnetId": "sn2"}
                    ],
                    "vulnerabilities": [
                        {"id": "3", "score": "6.8", "ports": ["22"]}
                    ]
                },
                {
                    "id": "superDB",
                    "name": "db-master",
                    "label": "db-master (LAN)",
                    "desc": "Internal Database Server",
                    "roles": ["InternalServer"],
                    "attributes": {"platform": "linux"},
                    "group": 2,
                    "locations": [
                        {"ip": "192.168.17.100", "subnetId": "sn2"}
                    ],
                    "vulnerabilities": [
                        {"id": "3", "score": "6.8", "ports": ["22"]}
                    ]
                }
            ],
            "vulnerabilities": [
                {
                    "id": "1",
                    "score": "7.3",
                    "externalId": "CVE-2013-0715",
                    "source": "CVE",
                    "cvss2": "7.3",
                    "shortDesc": "Login bypass (SQL injection)",
                    "description": "This vulnerability allows a remote attacker to bypass the PHP authentication process via an SQL injection attack and obtain access as a registered user.",
                    "type": "injection",
                    "requires": "none",
                    "provides": "app_user_priv",
                    "vector": "remote"
                },
                {
                    "id": "2",
                    "score": "9.5",
                    "externalId": "CVE-2015-0101",
                    "source": "CVE",
                    "cvss2": "9.5",
                    "shortDesc": "PHP command injection",
                    "description": "This vulnerability allows an authenticated user to inject system commands via malformed requests sent to the PHP server.",
                    "type": "injection",
                    "requires": "app_user_priv",
                    "provides": "sys_user_priv",
                    "vector": "local"
                },
                {
                    "id": "3",
                    "score": "6.8",
                    "externalId": "CVE-2009-1015",
                    "source": "CVE",
                    "cvss2": "6.8",
                    "shortDesc": "SSH buffer overflow",
                    "description": "This vulnerability allows a remote attacker to establish an SSH connection to the remote host via a buffer overflow insertion method.",
                    "type": "buffer_overflow",
                    "requires": "sys_user_priv",
                    "provides": "sys_root_priv",
                    "vector": "remote"
                },
                {
                    "id": "4",
                    "score": "9.3",
                    "externalId": "CVE-2017-6074",
                    "source": "CVE",
                    "cvss2": "9.3",
                    "cvss3": "7.8",
                    "shortDesc": "Privilege escalation",
                    "description": "The dccp_rcv_state_process function in net/dccp/input.c in the Linux kernel through 4.9.11 mishandles DCCP_PKT_REQUEST packet data structures in the LISTEN state, which allows local users to obtain root privileges or cause a denial of service (double free) via an application that makes an IPV6_RECVPKTINFO setsockopt system call.",
                    "type": "escalation",
                    "requires": "sys_user_priv",
                    "provides": "sys_root_priv",
                    "vector": "local"
                },
                {
                    "id": "5",
                    "score": "8.3",
                    "externalId": "51027",
                    "source": "NESSUS",
                    "shortDesc": "SMB unauthorized resource mapping R/W",
                    "description": "SMB unauthorized resource mapping R/W.",
                    "type": "buffer_overflow",
                    "requires": "sys_user_priv",
                    "provides": "sys_user_priv",
                    "vector": "remote"
                }
            ],
            "reachability": {
                "defaultPolicy": "DENY",
                "rules": [
                    {"source": ["inet"], "destination": ["fw1", "ws1_dmz", "db1_dmz", "mail1_dmz", "sysadmin1"],
                     "ports": ["22", "80", "8080"], "action": "ACCEPT"},
                    {"source": ["sysadmin1", "fw1", "ws1_dmz", "db1_dmz", "mail1_dmz"],
                     "destination": ["fw1", "ws1_dmz", "db1_dmz", "mail1_dmz"], "ports": ["*"], "action": "ACCEPT"},
                    {"source": ["sysadmin1", "ws1_dmz"], "destination": ["testing1"], "ports": ["*"],
                     "action": "ACCEPT"},
                    {"source": ["sysadmin1", "testing1"], "destination": ["ws1_internal"], "ports": ["*"],
                     "action": "ACCEPT"},
                    {"source": ["sysadmin1", "ws1_internal"], "destination": ["superDB"], "ports": ["*"],
                     "action": "ACCEPT"},
                    {"source": ["win1", "win2", "win3", "linux1", "linux2", "linux3"],
                     "destination": ["win1", "win2", "win3", "linux1", "linux2", "linux3"], "ports": ["*"],
                     "action": "ACCEPT"},
                    {"source": ["win1", "win2", "win3", "linux1", "linux2", "linux3"],
                     "destination": ["fw1", "ws1_dmz", "db1_dmz", "mail1_dmz", "testing1", "ws1_internal"],
                     "ports": ["*"],
                     "action": "ACCEPT"},
                    {"source": ["sn1", "sn2"], "destination": ["inet"], "ports": ["*"], "action": "ACCEPT"}
                ]
            }
        }
        demo_json = json.dumps(demo)
        logging.info('Start Interpret Network Details  ...'.format())
        self.network = self.interpreter.generateNetwork(demo_json)
        logging.info('Finish Interpret Network Details  ...'.format())
        self.generateGraph(True)
        self.fireDemoEvent()

    def generateGraph(self, demo=False):
        logging.info('Start Generating Attach Graph  ...'.format())
        answer = self.algorithm.generateAttackGraph(self.network, demo)
        self.rate = answer[0]
        self.graph = answer[1]
        logging.info('Finish Generating Attach Graph  ...'.format())
        logging.info('Network Rate is = {} .'.format(self.rate))
        return True

    def getShortPath(self, dest):
        logging.info('Start Finding Shortest Path  ...'.format())
        source = self.getNode(self.network, "Attacker's location", 'internet')
        if source is None:
            self.fireShortPathEvent('Path not found')
            return
        # target = self.getNode(self.network, dest)
        self.analysis.getShortestPath(self.graph, source, dest)
        logging.info('Finish Finding Shortest Path  ...'.format())
        self.fireShortPathEvent('')

    def getVulnerablePath(self, dest):
        logging.info('Start Finding Most Vulnerable Path  ...'.format())
        source = self.getNode(self.network, "Attacker's location", 'internet')
        if source is None:
            self.fireVulnerablePathEvent('Path not found')
            return
        # target = self.getNode(self.network, dest)
        self.analysis.getVulnerablePath(self.graph, source, dest)
        logging.info('Finish Finding Most Vulnerable Path ...'.format())
        self.fireVulnerablePathEvent('')

    def getExposeComponent(self):
        logging.info('Start Finding Most Expose Component ...'.format())
        self.analysis.getExposeComponent(self.graph)
        logging.info('Finish Finding Most Expose Component ...'.format())
        self.fireExposeComponentEvent('')

    def getNode(self, network, name, internet=''):
        if network["nodes"]:
            for node in network["nodes"]:
                if node.description.lower() == name.lower():
                    return node
                if internet != '':
                    if internet.lower() == node.name.lower():
                        return node
                    if internet.lower() == node.label.lower():
                        return node

    def setDB(self):
        answer = ''
        logging.info('Start Downloading Data Feeds From NVD Site ...'.format())
        try:
            self.dal.downloadNVD()
        except:
            answer = 'Error while downloading NVD Data Feeds, please check internet connection.'
            logging.info(answer.format())
            # self.fireDBEvent(answer)
        logging.info('Finish Downloading Data Feeds From NVD Site ...'.format())
        logging.info('Start Attach Data Feeds to MongoDB ...'.format())
        try:
            self.dal.createDB()
        except:
            answer = 'Error while establishing DB, please check if MongoDB installed or Connected.'
            logging.info(answer.format())
            # self.fireDBEvent(answer)
        logging.info('Finish Attach Data Feeds to MongoDB ...'.format())
        self.fireDBEvent(answer)

    def register(self, listener):
        self.listeners.add(listener)

    def fireDemoEvent(self):
        for listener in self.listeners:
            listener.demoFromModel(self.rate, self.network)

    def fireManualEvent(self):
        for listener in self.listeners:
            listener.manualFromModel(self.rate, self.network)

    def fireAutomaticEvent(self, answer):
        for listener in self.listeners:
            listener.automaticFromModel(self.rate, self.network, answer)

    def fireShortPathEvent(self, answer):
        for listener in self.listeners:
            listener.shortPathFromModel(answer)

    def fireVulnerablePathEvent(self, answer):
        for listener in self.listeners:
            listener.vulnerablePathFromModel(answer)

    def fireExposeComponentEvent(self, answer):
        for listener in self.listeners:
            listener.exposeComponentFromModel(answer)

    def fireDBEvent(self, answer):
        for listener in self.listeners:
            listener.finishedDBFromModel(answer)

    def __new__(cls, *args, **kwargs):
        if VSModel._instance is None:
            with Lock():
                if VSModel._instance is None:
                    VSModel._instance = super().__new__(cls, *args, **kwargs)
                    logging.info('----------------------------------------'.format())

        return VSModel._instance
