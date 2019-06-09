import json

class Reachability(object):

    def __init__(self, rules, defaultPolicy='DENY'):
        self._defaultPolicy = defaultPolicy
        self.rules = rules

    def __str__(self):
        string = json.dumps(self.rules)

        return "reachability : defaultPolicy : " + self._defaultPolicy + " rules : " + string
