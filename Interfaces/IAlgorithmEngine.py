import abc


class IAlgorithmEngine(abc.ABC):

    @abc.abstractmethod
    def generateAttackGraph(self, network, demo=False):
        pass

    @abc.abstractmethod
    def calcWeight(self):
        pass
