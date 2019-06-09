from threading import Lock
import networkx as nx
import Model.ReachabilityEngine as ReachabilityEngine
import Model.AnalysisEngine as AnalysisEngine
import Model.DAL as DAL
import time
import matplotlib.pyplot as plt


class AlgorithmEngine(object):
    _instance = None
    reachability = ReachabilityEngine.ReachabilityEngine()
    analysis = AnalysisEngine.AnalysisEngine()

    def generateAttackGraph(self, network, demo=False):
        """
        Building the attack graph of the network by a dict.
        """
        plt.close()
        counter = 0
        sum = 0
        G = nx.DiGraph()
        attackerInitialNode = self.getAttackerInitialNode(network)
        matrix = self.reachability.generateReachabilityMatrix(network)
        attackerNodes = set()
        attackerNodes.add(attackerInitialNode)
        # currentAV = "network"
        visitedNodes = list()
        labeldict = {}
        labeldict[attackerInitialNode] = attackerInitialNode.label
        lastNode = None
        while len(attackerNodes) > 0:
            curNode = attackerNodes.pop()
            lastNode = curNode
            G.add_node(lastNode)
            visitedNodes.append(curNode)
            v1 = curNode.vulnerabilities
            v1 = self.sortVul(v1)
            for v in v1:
                if demo is True:
                    vul = self.getVul(network["vulnerabilities"], v["id"])
                else:
                    vul = v
                if self.comparePriv(curNode.priv, vul.requires):
                    if self.comparePriv(vul.provides, curNode.priv):
                        curNode.priv = vul.provides
                        currentAV = vul.vector
                        G.add_node(vul)
                        weight = self.calcWeight(vul)
                        counter+=1
                        sum+=weight
                        G.add_edge(lastNode, vul, weight=weight)
                        lastNode = vul
                        if vul.shortDesc != '':
                            labeldict[vul] = vul.shortDesc
                        else:
                            labeldict[vul] = vul.cve
            destNodes = self.reachability.getReachableNodesFromNodes(matrix, curNode, network["nodes"])
            for n in destNodes:
                v2 = n.vulnerabilities
                for v in v2:
                    if demo is True:
                        vul = self.getVul(network["vulnerabilities"], v["id"])
                    else:
                        vul = v
                    # if Scanner.compareAV(currentAV,vul.vector):
                    if self.comparePriv("None", vul.requires) or self.comparePriv(curNode.priv, vul.requires):
                        # if self.comparePriv(vul.provides, n.priv):
                            n.priv = vul.provides
                            if vul.shortDesc != '':
                                 labeldict[vul] = vul.shortDesc
                            else:
                                 labeldict[vul] = vul.cve
                            G.add_node(vul)
                            weight = self.calcWeight(vul)
                            counter+=1
                            sum+=weight
                            G.add_edge(lastNode, vul, weight=weight)
                            G.add_node(n)
                            G.add_edge(vul, n)
                            if n.label != '':
                                labeldict[n] = n.label
                            else:
                                labeldict[n] = n.name
                            if n not in visitedNodes:
                                attackerNodes.add(n)
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, labels=labeldict, with_labels=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.savefig('Images//graph.png', format='PNG')
        result = 0
        if counter!= 0:
            result = sum/counter
        answer = [result, G]
        return answer

    def getVul(self, vulnerabilities, id):
        for vulen in vulnerabilities:
            if vulen.id == id:
                return vulen

    def calcWeight(self, vul):
        """
        Calculate the weight by : Complexity, Impact, Exploitability.
        """
        dal = DAL.DAL()
        cve = dal.getVulnerabilityByCVE(vul.cve)
        # print(cve)
        if cve is None:
            return 0
        complexity = 0
        exp = 0
        impact = 0
        if cve['impact']['baseMetricV2']['cvssV2']['accessComplexity'] is not None:
            complexity = cve['impact']['baseMetricV2']['cvssV2']['accessComplexity']
            complexity = self.complexityScore(complexity)
        if cve['impact']['baseMetricV2']['exploitabilityScore'] is not None:
            exp = cve['impact']['baseMetricV2']['exploitabilityScore']
        if cve['impact']['baseMetricV2']['impactScore'] is not None:
            impact = cve['impact']['baseMetricV2']['impactScore']
        try:
            weight = 0.2 * complexity + 0.4 * exp + 0.4 * impact
        except:
            weight = 0
        return weight

    def complexityScore(self, complexity):
        if complexity == 'High':
            return 1
        if complexity == 'MEDIUM':
            return 5
        if complexity == 'LOW':
            return 10

    def getAttackerInitialNode(self, network):
        if network["nodes"]:
            for node in network["nodes"]:
                if node.description == "Attacker's location" or node.name.lower() == 'internet':
                    return node

    def sortVul(self, vulnerabilities):
        n = len(vulnerabilities)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.comparePriv(vulnerabilities[j], [j+1]):
                    temp = vulnerabilities[j + 1]
                    vulnerabilities[j+1] = vulnerabilities[j]
                    vulnerabilities[j+1] = temp
        return vulnerabilities

    def comparePriv(self, priv1,priv2):
        if priv1 == "sys_root_priv":
            return True
        if priv1 == "sys_user_priv":
            if priv2 == "sys_root_priv":
                return False
            else:
                return True
        if priv1 == "app_admin_priv":
            if priv2 == "sys_root_priv" or priv2 == "sys_user_priv":
                return False
            else:
                return True
        if priv1 == "app_user_priv":
            if priv2 == "sys_root_priv" or priv2=="sys_user_priv" or priv2 =='app_admin_priv':
                return False
            else:
                return True
        if priv1 == "None/VNone" or priv1 == "None" or priv1 == "VNone" or priv1 == "none":
            if priv2 == "None/VNone" or priv2 == "None" or priv2 == "VNone" or priv2 == "none":
                return True
            else:
                return False

    def compareAV(self, av1, av2):
        if av1=="local":
            return True
        if av1=="remote":
            if av2 == "remote" or av2 =="network":
                return True;
            return False;
        if av1=="network":
            if av2=="network" or av2=='remote':
                return True;
            return False;

    def __new__(cls, *args, **kwargs):
        if AlgorithmEngine._instance is None:
            with Lock():
                if AlgorithmEngine._instance is None:
                    AlgorithmEngine._instance = super().__new__(cls, *args, **kwargs)

        return AlgorithmEngine._instance
