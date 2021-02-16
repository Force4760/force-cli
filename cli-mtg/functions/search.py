import scrython
def search(name: str, number: int = 0):
    """Search a card by name\n
       name -> str -> name of the card\n
       number -> int -> number of the card"""
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
        
        return card
    except:
        print("That card does not exist!")
        return None