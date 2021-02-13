import scrython
import json
import os

def add_card(name, deck, number):
    filename = f"./decks/{deck}.json"
    try:
        sd = scrython.cards.Named(exact=name)  

        try:
            power = sd.power()
        except:
            power = "none"

        try:
            tou = sd.toughness()
        except:
            tou = "none"

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
        
        
        with open(filename, 'r') as f:
            data = json.load(f)
            if name in data["Main Board"]:
                data["Main Board"][name]["number"] += number
            else:
                data["Main Board"][name] = card
               

        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
    except:
        "Sorry! I couldn't find this card or this deck.'"

add_card("Black Lotus", "elves_modern", 1)