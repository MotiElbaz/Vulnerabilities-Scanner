import abc


class IReasoningEngine(abc.ABC):

    @abc.abstractmethod
    def getPrivPost(self, desc, av, auth='', priv=''):
        pass

    @abc.abstractmethod
    def getPrivPre(self, desc, impact, privReq='', auth=''):
        pass

