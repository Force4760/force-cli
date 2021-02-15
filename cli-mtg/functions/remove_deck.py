import os

def delete(deck: str):
    """Delete a deck"""

    deckFileName = f"./decks/{deck}.json"

    resp = input("Are you sure you want to delete? (y) ")
    
    if resp == "y" or resp == "Y" or resp == "YES" or resp == "yes":
        try:
            os.remove(deckFileName)
            print("The deck was deleted!")
        except:
            print("The deck does not exist!")
    else:
        print("The deck was not deleted!")

delete("fsgs")