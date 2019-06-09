class Node(object):
    idGenerator = 0

    def __init__(self, name, label, description,  vulnerabilities, id=''):
        self.id = id
        self.name = name
        self.label = label
        self.description = description
        self.vulnerabilities = vulnerabilities
        self.priv = "None/VNone"
        self.av = "None"
        self.localID = self.__class__.idGenerator
        self.__class__.idGenerator += 1

    def __str__(self):
        vulnerabilitiesStr = ""
        for r in self.vulnerabilities:
            vulnerabilitiesStr += str(r)
        return "node : {Local ID : " +str(self.localID) +" , id : " + self.id + ", name : " + self.name + ", label : " + self.label + ", description : " + self.description + ", vulnerabilities : " + vulnerabilitiesStr + "}"
