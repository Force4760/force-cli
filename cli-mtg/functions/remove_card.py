import json
import os


def remove_card(name: str, deck: str, number: int = 0, section: str = "main"):
    """Removes a certain card (name) from a ceratin deck (deck)\n
       if no number is given the card will be removed\n
       if a number is given the number in that card will be lowered until it reaches zero\n
       name -> str -> name of the card\n
       deck -> str -> name of the deck\n
       number -> int -> number of cards to remove (if 0 all cards will be removed)\n
       section -> str -> section where the card is located (main/side/maybe)"""

    # check section
    if section.lower() == "side":
        sec = "Side Board"
    elif section.lower() == "maybe":
        sec = "Maybe Board"
    else:
        sec = "Main Board"

    file_name = f"./decks/{deck}.json"

    try:
        # if number is given
        if number:

            # open file
            with open(file_name, 'r') as f:
                data = json.load(f)
                if name in data[sec]:
                    data[sec][name]["number"] -= number
                    if data[sec][name]["number"] <= 0:
                        data[sec].pop(name)
                else:
                    print("Sorry! That card is not on that deck.")

            # recreate file
            os.remove(file_name)
            with open(file_name, 'w') as f:
                json.dump(data, f, indent=4)

        # completely remove the card
        else:
            with open(file_name, 'r') as f:
                data = json.load(f)
                if name in data[sec]:
                    data[sec].pop(name)
                else:
                    print("Sorry! That card is not on that deck.")

            os.remove(file_name)
            with open(file_name, 'w') as f:
                json.dump(data, f, indent=4)

    except:
        "Sorry! I couldn't find this card or this deck.'"


if __name__ == "__main__":
    remove_card("rrrrr", "elv", 2)

