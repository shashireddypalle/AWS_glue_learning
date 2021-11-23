import json

class getConfigParser():
    def __init__(self, path):
        config = json.load(path)
        return config

    def sourceDetails(self):
        pass

    def targetDetails(self):
        pass

    def sourceType(self):
        pass

    def targetType(self):
        pass