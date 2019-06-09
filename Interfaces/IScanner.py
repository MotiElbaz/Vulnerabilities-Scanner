import abc


class IScanner(abc.ABC):

    @abc.abstractmethod
    def scan(self, subnets):
        pass
