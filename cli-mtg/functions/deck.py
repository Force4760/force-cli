import os
import json
import webbrowser


def show(deck: str):
    file_name = f"./decks/{deck}.json"
    if os.path.isfile(file_name):
        final = """
        <!DOCTYPE html>
        <html lang='en'>
        <head>
            <meta charset='UTF-8'>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <link rel='stylesheet' href='../web/style.css'>
            <title>Deck</title>
        </head>
        <body>
            <header>
        """
        with open(file_name, 'r') as f:
            data = json.load(f)
            deck_name = f"<h1>{data['Name']}</h1>"
            deck_form = f"<h2 class='format'>{data['Format']}</h2>"
            final += deck_name
            final += deck_form
            final += """
                </header>
                <main>
                    <div id="card-view"></div>
                    <div class='list'>
                        <h2>Main Board</h2>
            """
            for i in data["Main Board"]:
                name = data["Main Board"][i]["name"]
                number = data["Main Board"][i]["number"]
                cost = data["Main Board"][i]["cost"]
                img = data["Main Board"][i]["image"]
                ht = f"<a href='{img}' target='_blank'><span class='number'>{number}</span>&nbsp;&nbsp;&nbsp;&nbsp; {name} &nbsp;&nbsp;&nbsp;&nbsp;<span class='cost'>{cost}</span></a>"
                final += ht
            final += "<h2>Side Board</h2>"
            for i in data["Side Board"]:
                name = data["Side Board"][i]["name"]
                number = data["Side Board"][i]["number"]
                cost = data["Side Board"][i]["cost"]
                img = data["Side Board"][i]["image"]
                ht = f"<a href='{img}' target='_blank'><span class='number'>{number}</span>&nbsp;&nbsp;&nbsp;&nbsp; {name} &nbsp;&nbsp;&nbsp;&nbsp;<span class='cost'>{cost}</span></a>"
                final += ht

            final += """</div>
                </main>
                <script src="../web/main.js"></script>
            </body>
            </html>"""

        with open(f"./exports/{deck}.html", "w") as f:
            f.write(final)

        webbrowser.open(f"./exports/{deck}.html")

    else:
        print("Sorry! That deck does not exist!")


if __name__ == "__main__":
    show("elves_modern")

