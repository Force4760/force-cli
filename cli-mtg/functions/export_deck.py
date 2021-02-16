import json

def export_deck(name: str):
    """Export a certain deck as a .txt file on the ./exports folder\n
    name -> str -> the name of the deck"""
    try:
        deck_file_name = f"./decks/{name}.json"
        export_name = f"./exports/{name}.txt"
        main_board = ""
        side_board = ""

        # open the deck file
        with open(deck_file_name, "r") as f:
            data = json.load(f)
            for i in data["Main Board"]:
                main_board += f"{data['Main Board'][i]['number']} {data['Main Board'][i]['name']}\n"
            for i in data["Side Board"]:
                side_board += f"{data['Side Board'][i]['number']} {data['Side Board'][i]['name']}\n"

        with open(export_name, "w+") as f:
            f.write("Main Board\n")
            f.write(main_board)
            f.write("\nSide Board\n")
            f.write(side_board)      
    except:
        print("Sorry! Either that deck does not exist or something went wrong.\n")

if __name__ == "__main__":
    export_deck("elv_modern")