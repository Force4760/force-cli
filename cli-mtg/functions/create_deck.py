import json
import os

def create_deck(name, form):
    if not name:
        print("Sorry! I couldn't understand.'")
    else:
        fileName = f"decks/{name}.json"
        if os.path.isfile(fileName):
            print("Sorry! That Deck already exists. Please choose a new name.\n")
        else:      
            deck = {
                "Name": name,
                "Format": form,
                "Main Board": {},
                "Side Board": {},
                "Maybe Board": {},
            }
            with open(fileName, 'w') as f:
                json.dump(deck, f, indent=4)
            print(f"The deck {name} for the {form} format was successfully created!\n")

if __name__ == '__main__':
    create_deck("elve", "modern")