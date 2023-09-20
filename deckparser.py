import card

class DeckParser:   
    def __init__(self):
        pass
    
    def merge(self, path1, path2, outPath):
        with open(outPath, "w") as out:
            deck1 = {}
            deck2 = {}

                     
    def parseFile(self, path):
        with open(path, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.split()
                count = line[0]
                name = line[1]
                pos = 2
                while not line[pos].startswith("("):
                    name.append(" " + line[pos])
                    pos += 1
                set = line[pos]
                id = line[pos + 1]
                
                    
                
                