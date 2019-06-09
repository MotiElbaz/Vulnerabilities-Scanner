import abc


class IDAL(abc.ABC):

    @abc.abstractmethod
    def downloadNVD(self):
        pass

    @abc.abstractmethod
    def createDB(self):
        pass

    @abc.abstractmethod
    def getVulnerabilityByName(self, name, version):
        pass

    @abc.abstractmethod
    def getVulnerabilityByCVE(self, cve_id):
        pass
