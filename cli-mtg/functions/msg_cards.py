import scrython

def s_no_result(name:str)-> list:
    card_list = scrython.cards.Autocomplete(q=name)
    j = 1
    msg = {}
    for i in card_list.data():
        msg[str(j)] = i.replace("'", "")
        j+=1
    
    m = ""
    for i in msg:
        m += "\n  "+ i + "- "+ msg[i]
    return [msg, m]