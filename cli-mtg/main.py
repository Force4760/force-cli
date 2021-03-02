from functions.add_card import add_card
from functions.advanced import advanced
from functions.remove_card import remove_card
from functions.msg_cards import s_no_result
from functions.search import search, full_search
from functions.create_deck import create_deck
from functions.export_deck import export_deck
from functions.remove_deck import delete
from functions.update import update
from functions.deck import show


def del_deck():
    name = input("Name -> ")
    delete(name)


def add():
    name = input("Name -> ")
    number = input("Number -> ")
    deck = input("Deck -> ")
    board = input("Board -> ")

    if board != "side" or board != "maybe":
        board = "main"
    try:
        add_card(name, deck, int(number), board)
    except:
        print("Sorry! Something went wrong")


def remove():
    name = input("Name -> ")
    number = input("Number -> ")
    deck = input("Deck -> ")
    board = input("Board -> ")

    if board != "side" or board != "maybe":
        board = "main"
    try:
        remove_card(name, deck, int(number), board)
    except:
        print("Sorry! Something went wrong")


def sea():
    name = input("Name -> ")
    print(full_search(name))


def create():
    name = input("Name -> ")
    form = input("Format -> ")
    if name.replace(" ", ""):
        create_deck(name.replace(" ", ""), form)
    else:
        print("You need to provide a name")


def s():
    name = input("Name -> ")
    show(name)


def up():
    name = input("Name -> ")
    update(name)


def export():
    name = input("Name -> ")
    export_deck(name)


if __name__ == "__main__":
    while True:
        cmd = input("-> ")
        if cmd == "add":
            add()
            continue
        elif cmd == "advanced":
            advanced()
            continue
        elif cmd == "remove":
            remove()
            continue
        elif cmd == "search":
            sea()
            continue
        elif cmd == "create":
            create()
            continue
        elif cmd == "export":
            export()
            continue
        elif cmd == "delete":
            del_deck()
            continue
        elif cmd == "update":
            up()
            continue
        elif cmd == "show":
            s()
            continue
        elif cmd == "e":
            break
