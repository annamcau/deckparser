class Card:
    BASICS = {"Plains", "Swamp", "Island", "Mountain", "Forest", "Wastes", "Cloud"}
    
    def __init__(self, count, name, set, id):
        self._num = count
        self._name = name
        self._set = set
        self._id = id
        
    def __str__(self):
        return self._num + " " + self._name + " " + self._set + " " + self._id
    
    def getCount(self):
        return int(self._num)
    
    def getName(self):
        return self._name
    
    def getSet(self):
        return self._set
    
    def getId(self):
        return self._id
    
    def isBasic(self):
        return self._name in self.BASICS
        
    