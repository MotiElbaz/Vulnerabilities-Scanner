class Subnet(object):

    def __init__(self, id, name, description, ipRange):
        self.id = id
        self.name = name
        self.description = description
        self.ipRange = ipRange

    def __str__(self):
        return "subnet : {id : " + self.id + ", name : " + self.name + ", description : " + self.description + ", ipRange : " + self.ipRange + "}"
