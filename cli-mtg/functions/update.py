import os
from functions.search import search
from tqdm import tqdm
import json


def update(deck: str = ""):
    """Update info on every card\n
       if no (deck) is given all decks will be updated\n
       deck -> str -> name of the deck to update"""

    if deck:
        file_name = f"./decks/{deck}.json"
        if os.path.isfile(file_name):
            with open(file_name, 'r') as f:
                data = json.load(f)
                print("Main Board")
                for i in tqdm(data["Main Board"]):
                    name = data["Main Board"][i]["name"]
                    number = data["Main Board"][i]["number"]
                    card = search(name)
                    if card:
                        data["Main Board"][i] = card
                        data["Main Board"][i]["number"] = number
                print("Side Board")
                for i in tqdm(data["Side Board"]):
                    name = data["Side Board"][i]["name"]
                    number = data["Side Board"][i]["number"]
                    card = search(name)
                    if card:
                        data["Side Board"][i]["number"] = number
                        data["Side Board"][i] = card
                print("Maybe Board")
                for i in tqdm(data["Maybe Board"]):
                    name = data["Maybe Board"][i]["name"]
                    number = data["Maybe Board"][i]["number"]
                    card = search(name)
                    if card:
                        data["Maybe Board"][i]["number"] = number
                        data["Maybe Board"][i] = card

            os.remove(file_name)
            with open(file_name, 'w') as f:
                json.dump(data, f, indent=4)

        else:
            print("Sorry! That deck does not exist!")


if __name__ == "__main__":
    update("elves_modern")
