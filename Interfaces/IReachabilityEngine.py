import abc


class IReachabilityEngine(abc.ABC):

    @abc.abstractmethod
    def generateReachabilityMatrix(self, network):
        pass

    @abc.abstractmethod
    def getReachableNodesFromNodes(self, matrix, node, nodes):
        pass

