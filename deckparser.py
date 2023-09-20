import card

class DeckParser:   
    def __init__(self):
        pass
    
    def merge(self, path1, path2, outPath):
        with open(outPath, "w") as out:
            deck1 = {}
            deck2 = {}
            with open(path1, "r") as file1:
                lines1 = file1.readlines()
                for line in lines1:
                    pass
                
            with open(path2, "r") as file2:
                lines2 = file2.readlines()
                     
                    