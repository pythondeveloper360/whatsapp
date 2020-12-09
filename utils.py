class strToDict(dict):
    def __init__(self, string):
        self.string = string
        self.s = self.string.replace('{', '').replace('}', '').replace(
            " ", "").replace("'", "").replace('"', "").split(',')
        self.data = {self.s[i].split(":")[1]: self.s[i].split(":")[
            0] for i in range(len(self.s))}

    def __repr__(self):
        return str(self.data)

    def update(self, obj):
        self.data.update(obj)
        return self.data
    def str(self):
        return str(self.data)
