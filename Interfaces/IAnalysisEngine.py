import abc


class IAnalysisEngine(abc.ABC):

    @abc.abstractmethod
    def getShortestPath(self, network, demo=False):
        pass

    @abc.abstractmethod
    def getVulnerablePath(self, graph, source, target):
        pass

    @abc.abstractmethod
    def getExposeComponent(self, graph):
        pass
