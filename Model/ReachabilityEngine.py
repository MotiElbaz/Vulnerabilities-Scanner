from threading import Lock
import numpy as numpy
import logging

logging.basicConfig(filename='LOG.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
# TO DO : Reachability Matrix , need to consider the open ports , now its take in assumption that all ports are open
# instead of 1 will put list of ports


class ReachabilityEngine(object):
    _instance = None

    def generateReachabilityMatrix(self, network):
        """
        Build a reachability matrix according to the rules.
        """
        matrix = numpy.zeros((len(network["nodes"]), len(network["nodes"])))
        if network["reachabilities"]:
            reach = network["reachabilities"][0]
            for rule in reach.rules:
                for source in rule["source"]:
                    sourceNode = [x for x in network["nodes"] if x.id.lower() == source.lower()]
                    if len(sourceNode) == 0:
                        sourceNode = [x for x in network["nodes"] if x.name.lower() == source.lower()]
                    if len(sourceNode) > 0:
                        for destination in rule["destination"]:
                            destinationNode = [x for x in network["nodes"] if x.id.lower() == destination.lower()]
                            if len(destinationNode) == 0:
                                destinationNode = [x for x in network["nodes"] if x.name.lower() == destination.lower()]
                            if len(destinationNode) > 0:
                                matrix[sourceNode[0].localID][destinationNode[0].localID] = 1
        return matrix

    def getReachableNodesFromNodes(self, matrix, node, nodes):
        """
        Create a list with all the nodes reachable from specific node.
        """
        row = node.localID
        destNodes = list()
        for i in range(len(matrix[row])):
            if row != i:
                if matrix[row][i] == 1:
                    for n in nodes:
                        if n.localID == i:
                            destNodes.append(n)
        return destNodes

    def __new__(cls, *args, **kwargs):
        if ReachabilityEngine._instance is None:
            with Lock():
                if ReachabilityEngine._instance is None:
                    ReachabilityEngine._instance = super().__new__(cls, *args, **kwargs)

        return ReachabilityEngine._instance
