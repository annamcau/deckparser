class DeckParser:
    BASICS = "Plains, Swamp, Island, Mountain, Forest"
    
    def __init__(self):
        pass
    
    def merge(self, path1, path2, outPath):
        with open(outPath, "w") as out:
            with open(path1, "r") as file1:
                with open(path2, "r") as file2:
                    cards = []
                    