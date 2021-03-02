import scrython
from functions.msg_cards import s_no_result


def search(name: str) -> str:
    """Search a card by name\n
       name -> str -> name of the card\n
    """
    sd = scrython.cards.Named(fuzzy=name)  # get card

    name = sd.name()
    color = sd.color_identity()
    typeline = sd.type_line()
    cmc = sd.cmc()
    power = get_power(sd)
    tou = get_tou(sd)
    try:
        loyalty = sd.loyalty()
    except:
        loyalty = ""
    legality = sd.legalities()
    image = sd.image_uris(0, "small")
    cost = get_cost(sd)
    uri = sd.scryfall_uri()

    card = {
        "name": name,
        "color": color,
        "typeline": typeline,
        "cmc": cmc,
        "cost": cost,
        "power": power,
        "toughness": tou,
        "loyalty": loyalty,
        "legality": legality,
        "image": image,
        "uri": uri
    }
    return card


def get_cost(sd):
    try:
        cost = sd.mana_cost()
    except:
        try:
            cost = sd.card_faces()[0]["mana_cost"] + \
                "/" + sd.card_faces()[1]["mana_cost"]
        except:
            cost = ""
    return cost


def get_power(sd):
    try:
        power = sd.power()
    except:
        try:
            power = sd.card_faces()[0]["power"] + "-" + \
                sd.card_faces()[1]["power"]
        except:
            power = ""
    return power


def get_tou(sd):
    try:
        tou = sd.toughness()
    except:
        try:
            tou = sd.card_faces()[0]["toughness"] + "-" + \
                sd.card_faces()[1]["toughness"]
        except:
            tou = ""
    return tou


def full_search(name: str):
    try:
        card = search(name)
        return card
    except:
        m = s_no_result(name)
        msg = m[1]
        results = m[0]
        if len(results) == 0:
            print("Sorry I don't know that card.")
        else:
            print(msg)
            c = input("What Card? -> ")
            try:
                card = search(results[c].replace("'", ""))
                return card
            except:
                print("Sorry I don't know that card.")


if __name__ == "__main__":
    full_search("Black")
