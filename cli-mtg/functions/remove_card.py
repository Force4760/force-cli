import json
import os

def remove_card(name, deck, number = None):
    filename = f"./decks/{deck}.json"
    try:
        if number:
            
        
            with open(filename, 'r') as f:
                data = json.load(f)
                if data["Main Board"][name]:
                    data["Main Board"][name]["number"] -= number
                else:
                    print("Sorry! That card is not on that deck.")

            os.remove(filename)
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            
        else: 
            with open(filename, 'r') as f:
                data = json.load(f)
                if name in data["Main Board"]:
                    data["Main Board"].pop(name)
                else:
                    print("Sorry! That card is not on that deck.")

            os.remove(filename)
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

    except:
        "Sorry! I couldn't find this card or this deck.'"

if __name__ == "__main__":
    remove_card("Black Lotus", "elves_modern")