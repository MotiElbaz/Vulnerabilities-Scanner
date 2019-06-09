from Objects.Subnet import Subnet
from Objects.Node import Node
from Objects.Vulnerability import Vulnerability
from Objects.Reachability import Reachability
import Model.DAL as DAL
import Model.ReasoningEngine as ReasoningEngine
from threading import Lock
import json


class Interpreter(object):
    _instance = None
    dal = DAL.DAL()

    def generateNetwork(self, myString):
        """
        Create the data structure from a json.
        """
        Node.idGenerator = 0
        objects = json.loads(myString)
        network = dict()
        subnets = []
        nodes = []
        network["subnets"] = []
        network["nodes"] = []
        network["vulnerabilities"] = []
        network["reachabilities"] = []
        if objects["subnets"]:
            for subnet in objects["subnets"]:
                newSubnet = Subnet(subnet["id"], subnet["name"], subnet["desc"], subnet["ipRange"])
                subnets.append(newSubnet)
            network["subnets"] = subnets
        if objects["nodes"]:
            for n in objects["nodes"]:
                newNode = Node(n["name"], n["label"], n["desc"], n["vulnerabilities"], n["id"])
                network["nodes"].append(newNode)
        if objects["vulnerabilities"]:
            for vul in objects["vulnerabilities"]:
                newVul = Vulnerability(vul["externalId"], vul["shortDesc"], vul["description"],
                                       vul["requires"], vul["provides"], vul["vector"], vul["id"])
                network["vulnerabilities"].append(newVul)
        if objects["reachability"]:
            if objects["reachability"]["rules"]:
                newRules = []
                for rule in objects["reachability"]["rules"]:
                    newRules.append(rule)
                newRechability = Reachability(newRules, objects["reachability"]["defaultPolicy"])
                network["reachabilities"].append(newRechability)

        return network

    def generateNetworkManual(self, myString):
        Node.idGenerator = 0
        engine = ReasoningEngine.ReasoningEngine()
        objects = json.loads(myString)
        network = dict()
        subnets = []
        nodes = []
        network["subnets"] = []
        network["nodes"] = []
        network["reachabilities"] = []
        if objects["subnets"]:
            for subnet in objects["subnets"]:
                newSubnet = Subnet(subnet["id"], subnet["name"], subnet["desc"], subnet["ipRange"])
                subnets.append(newSubnet)
            network["subnets"] = subnets
        if objects["nodes"]:
            for n in objects["nodes"]:
                vulens = []
                for cve in n["vulnerabilities"]:
                    cve_data = self.dal.getVulnerabilityByCVE(cve)
                    if cve_data is not None:
                        cve_id = cve_data['cve']['CVE_data_meta']['ID']
                        cve_desc = cve_data['cve']['description']['description_data'][0]['value']
                        impact = cve_data['impact']['baseMetricV2']['cvssV2']['availabilityImpact']
                        cve_av = cve_data['impact']['baseMetricV2']['cvssV2']['accessVector']
                        auth = cve_data['impact']['baseMetricV2']['cvssV2']['authentication']
                        priv = ''
                        try:
                            priv = cve_data['impact']['baseMetricV3']['cvssV3']['privilegesRequired']
                        except:
                            e = ''
                            #print("No cvss3")
                        if priv != '':
                            auth = ''
                        cve_requires = engine.getPrivPost(cve_desc, cve_av, auth, priv)
                        cve_provides = engine.getPrivPre(cve_desc, impact, cve_requires)
                        tempVul = Vulnerability(cve_id, '', cve_desc, cve_requires, cve_provides, cve_av)
                        vulens.append(tempVul)
                newNode = Node(n["name"], n["label"], n["desc"], vulens)
                network["nodes"].append(newNode)
        if objects["reachability"]:
            if objects["reachability"]["rules"]:
                newRules = []
                for rule in objects["reachability"]["rules"]:
                    newRules.append(rule)
                newRechability = Reachability(newRules, objects["reachability"]["defaultPolicy"])
                network["reachabilities"].append(newRechability)

        return network

    def __new__(cls, *args, **kwargs):
        if Interpreter._instance is None:
            with Lock():
                if Interpreter._instance is None:
                    Interpreter._instance = super().__new__(cls, *args, **kwargs)

        return Interpreter._instance

