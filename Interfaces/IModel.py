import abc


class IModel(abc.ABC):

    @abc.abstractmethod
    def auto(self, subnets):
        pass

    @abc.abstractmethod
    def manual(self, network_json):
        pass

    @abc.abstractmethod
    def demo(self):
        pass

    @abc.abstractmethod
    def generateGraph(self, demo=False):
        pass

    @abc.abstractmethod
    def getVulnerablePath(self, dest):
        pass

    @abc.abstractmethod
    def getExposeComponent(self):
        pass

    @abc.abstractmethod
    def setDB(self):
        pass

    @abc.abstractmethod
    def register(self, listener):
        pass

