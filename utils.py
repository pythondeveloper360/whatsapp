
class Converter:
    def __init__(self, _list):
        self._list = _list
        self.data = []
    def __repr__(self):
        return str(self._list)

    def _dict(self):        
        for i in self._list:
            x = i.replace("{","").replace("}","").split(":")
            self.data.append(dict(id = x[0],name = x[1]))
        return self.data
    def append(self,obj):
        self.data.append(obj)
        return self.data
    