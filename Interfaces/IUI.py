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
    def shortPathFromModel(self):
        pass

    @abc.abstractmethod
    def vulnerablePathFromModel(self):
        pass

    @abc.abstractmethod
    def exposeComponentFromModel(self):
        pass

    @abc.abstractmethod
    def setDB(self):
        pass

    @abc.abstractmethod
    def register(self, listener):
        pass

