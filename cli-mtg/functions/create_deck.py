import json
import os


def create_deck(name: str, form: str = "free"):
    """Create a deck with the given name (name) and for the specified format (form)\n
       if the deck already exists it throws an exception\n
       name -> str -> name of the deck\n
       form -> str -> format of the deck (defaults to free)"""

    if not name:  # check if name was given (ie not "")
        print("Sorry! I couldn't understand.'")
    else:
        file_name = f"decks/{name}.json"
        if os.path.isfile(file_name):  # check if deck already exists
            print("Sorry! That Deck already exists. Please choose a new name.\n")
        else:
            # deck object
            deck = {
                "Name": name,
                "Format": form,
                "Main Board": {},
                "Side Board": {},
                "Maybe Board": {},
            }
            # open file
            with open(file_name, 'w') as f:
                json.dump(deck, f, indent=4)
            print(
                f"The deck {name} for the {form} format was successfully created!\n")


if __name__ == '__main__':
    create_deck("elve", "modern")

