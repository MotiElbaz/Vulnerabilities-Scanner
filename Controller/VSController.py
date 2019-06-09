import Model.VSModel as Model
#import View.UI as UI


class VSController(object):
    model = None
    ui = None

    def __init__(self, model, ui):
        self.ui = ui
        self.model = model
        self.model.register(self)
        self.ui.register(self)

    def demoFromModel(self, rate, network):
        self.ui.demoFromModel(rate, network)

    def manualFromModel(self, rate, network):
        self.ui.manualFromModel(rate, network)
        return

    def automaticFromModel(self, rate, network, answer):
        self.ui.autoFromModel(rate, network, answer)
        return

    def shortPathFromModel(self, answer):
        self.ui.shortPathFromModel(answer)
        return

    def vulnerablePathFromModel(self, answer):
        self.ui.vulnerablePathFromModel(answer)
        return

    def exposeComponentFromModel(self, answer):
        self.ui.exposeComponentFromModel(answer)
        return

    def finishedDBFromModel(self, answer):
        self.ui.setDB(answer)

    def demoFromUI(self):
        self.model.demo()

    def manualFromUI(self, network_json):
        self.model.manual(network_json)

    def automaticFromUI(self, subnets):
        self.model.auto(subnets)

    def shortPathFromUI(self, target):
        self.model.getShortPath(target)

    def vulnerablePathFromUI(self, target):
        self.model.getVulnerablePath(target)

    def exposeComponentFromUI(self):
        self.model.getExposeComponent()

    def setDBFromUI(self):
        self.model.setDB()

