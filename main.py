import sys
import deckparser

if __name__ == "__main__":
    args = []
    if len(sys.argv) > 1:
        # additional args
        for arg in sys.argv[1:]:
            args.append(arg)
    
    obj = deckparser.DeckParser()
    if args[0] == "merge":
        if len(args) > 3:
            obj.merge(args[1], args[2], args[3])
        else:
            print("Insufficient filename args for function 'merge'")
    else:
        print("Invalid function")