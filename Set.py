import json

class Set():
    def __init__(self,path=None):
        self.path = path
        if not path is None:
            self._load()

    def _load(self,path = None):
        if path is None:
            with open(self.path,'r') as file:
                raw_data = json.load(file)
                self.raw_data = raw_data
            self.fields = [field for field in raw_data.keys()]
            print(self.fields)

set = Set('Set/Set.json')
