from functions.search import full_search
import json
import os


def add_card(name: str, deck: str, number: int = 1, section: str = "main"):
    """Adds a card (card) to a specified deck (deck)\n
       if the card is already on the deck it will add the (number) to the current number on the card\n
       name -> str -> name of the card\n
       deck -> str -> name of the deck\n
       number -> int -> number of cards to add (defaults to 1)\n
       section -> str -> section to put the card (main/side/maybe)
    """
    # check section
    if section.lower() == "side":
        sec = "Side Board"
    elif section.lower() == "maybe":
        sec = "Maybe Board"
    else:
        sec = "Main Board"

    file_name = f"./decks/{deck}.json"
    try:
        # open deck file
        with open(file_name, 'r') as f:
            data = json.load(f)
            if name in data[sec]:  # if is already on the deck
                data[sec][name]["number"] += number
            else:
                card = full_search(name)
                if card:
                    data[sec][name] = card
                    data[sec][name]["number"] = number
        # recreate file
        os.remove(file_name)
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)

    except:
        "Sorry! I couldn't find this card or this deck.'"


if __name__ == "__main__":
    add_card("Island", "elves_modern", 3, "main")
