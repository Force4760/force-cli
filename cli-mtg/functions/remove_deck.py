import os

def delete(deck: str):
    """Delete a deck\n
       deck -> str -> name of the deck"""

    deck_file_name = f"./decks/{deck}.json"

    # ask confirmation
    resp = input("Are you sure you want to delete? (y) ")
    
    # check answer
    if resp == "y" or resp == "Y" or resp == "YES" or resp == "yes":
        try: # remove deck
            os.remove(deck_file_name)
            print("The deck was deleted!")
        except: # deck does not exist
            print("The deck does not exist!")
    else:
        print("The deck was not deleted!")

if __name__ == "__main__":
    delete("fsgs")