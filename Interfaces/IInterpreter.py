import abc


class IInterpreter(abc.ABC):

    @abc.abstractmethod
    def generateNetwork(self, network_json):
        pass

