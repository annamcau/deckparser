import argparse
import deckparser

if __name__ == "__main__":
    args = []
    parser = argparse.ArgumentParser(description="Parses decks for use in merging")
    parser.add_argument('func', type=str, help="Determines function of deckparser (currently only merge)")
    parser.add_argument('path1', type=str, help="Name of first input decklist (MTGO Format)")
    parser.add_argument('path2', type=str, help="Name of second input decklist (MTGO Format)")
    parser.add_argument('out', type=str, help="Output path for resulting merged list")
    args = parser.parse_args()
    
    obj = deckparser.DeckParser()
    if args.func == "merge":
        if args.path1 and args.path2 and args.out:
            obj.merge(args.path1, args.path2, args.out)
        else:
            print("Insufficient filename args for function 'merge'")
    else:
        print("Invalid function")