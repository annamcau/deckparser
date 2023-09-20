class Card:
    BASICS = {"Plains", "Swamp", "Island", "Mountain", "Forest", "Wastes", "Cloud"}
    
    def __init__(self, name, set, id):
        self._name = name
        self._set = set
        self._id = id
    
    def getName(self):
        return self._name
    
    def getSet(self):
        return self._set
    
    def getId(self):
        return self._id
    
    def isBasic(self):
        return self._name in self.BASICS
        
    