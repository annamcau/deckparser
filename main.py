import sys

class DeckParser:
    def __init__(self):
        pass
    
    def merge(self, path1, path2):
        pass

if __name__ == "__main__":
    args = []
    if len(sys.argv) > 1:
        # additional args
        for arg in sys.argv[1:]:
            args.append(arg)
    
    obj = DeckParser()
    if args[0] == "merge":
        if len(args) > 2:
            obj.merge(args[1], args[2])
        else:
            print("Insufficient filename args for function 'merge'")
    else:
        print("Invalid function")