import scrython
import json
import os

def add_card(name: str, deck: str, number: int = 1, section: str = "main" ):
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


    filename = f"./decks/{deck}.json"
    try:
        sd = scrython.cards.Named(exact=name) # get card  

        try: # some cards don't have power
            power = sd.power() 
        except:
            power = "none"

        try: # some cards don't have toughness
            tou = sd.toughness()
        except:
            tou = "none"

        # card object
        card = {
                "number": number,
                "name": sd.name(),
                "typeline": sd.type_line(),
                "power": power,
                "toughness" :  tou,
                "text": sd.oracle_text(),
                "cmc": sd.cmc(),
                "image": sd.image_uris(0, "normal"),
                "cost": sd.mana_cost(),
                "color": sd.color_identity(),
                "set": sd.set_name(),
                "legality": sd.legalities()
            }
        
        # open deck file
        with open(filename, 'r') as f:
            data = json.load(f)
            if name in data[sec]: # if is already on the deck
                data[sec][name]["number"] += number
            else:
                data[sec][name] = card
               
        # recreate file
        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
    except:
        "Sorry! I couldn't find this card or this deck.'"


if __name__ == "__main__":
    add_card("Black Lotus", "elves_modern", 3, "main")