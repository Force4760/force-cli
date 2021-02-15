import json

def export_deck(name: str):
    """Export a certain deck as a .txt file on the ./exports folder\n
    name -> str -> the name of the deck"""
    try:
        deckFileName = f"./decks/{name}.json"
        exportName = f"./exports/{name}.txt"
        mainboard = ""
        sideboard = ""

        # open the deck file
        with open(deckFileName, "r") as f:
            data = json.load(f)
            for i in data["Main Board"]:
                mainboard += f"{data['Main Board'][i]['number']} {data['Main Board'][i]['name']}\n"
            for i in data["Side Board"]:
                sideboard += f"{data['Side Board'][i]['number']} {data['Side Board'][i]['name']}\n"

        with open(exportName, "w+") as f:
            f.write("Main Board\n")
            f.write(mainboard)
            f.write("\nSide Board\n")
            f.write(sideboard)      
    except:
        print("Sorry! Either that deck does not exist or something went wrong.\n")

if __name__ == "__main__":
    export_deck("elv_modern")