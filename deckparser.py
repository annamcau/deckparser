import card

class DeckParser:   
    def __init__(self):
        pass
    
    def merge(self, path1, path2, outPath):
        with open(outPath, "w") as out:
            deck1 = self.parseFile(path1)
            deck2 = self.parseFile(path2)
            result = []
            for item in deck1:
                if item in deck2 and deck1[item].isBasic():
                    result.append(card.Card(str(max(deck1[item].getCount(), deck2[item].getCount())), item, deck1[item].getSet(), deck1[item].getId()))
                    del deck2[item]
                else:
                    result.append(card.Card("1", item, deck1[item].getSet(), deck1[item].getId()))
                    if item in deck2:
                        del deck2[item]
            for item in deck2:
                result.append(card.Card("1", item, deck2[item].getSet(), deck2[item].getId()))
            for item in result:
                out.write(str(item) + "\n")

                     
    def parseFile(self, path):
        with open(path, "r") as file:
            lines = file.readlines()
            deck = dict()
            for line in lines:
                line = line.split()
                count = line[0]
                name = line[1]
                pos = 2
                while not line[pos].startswith("("):
                    name += " " + line[pos]
                    pos += 1
                set = line[pos]
                id = line[pos + 1]
                newCard = card.Card(count, name, set, id)
                deck[newCard.getName()] = newCard
            return deck
                
                    
                
                