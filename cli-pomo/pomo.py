errorStr = "\nSorry your input could not be processed correctly, please try again!\n"
filename = './data/settings.json'
db = './data/db.json'

def clear(): #clear console 
    os.system('clear')

def helping(): #if argv is --help or -h
    signature = r""" 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    #  _______     _______     _______      _______     _______   # 
    # |  _____|   |  ___  |   |  ___  |    |  _____|   |  _____|  # 
    # | |___      | |   | |   | |___| |    | |         | |_____   # 
    # |  ___|     | |   | |   |  ___  |    | |         |  _____|  # 
    # | |         | |___| |   | |   \ \    | |_____    | |_____   # 
    # |_|         |_______|   |_|    \_\   |_______|   |_______|  # 
    #                                                             # 
    # Made by Force4760                                           # 
    #                                                             # 
    # Start Date:  8/2/2021                                       # 
    # Description: Pomodoro CLI App                               #  
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    """
    print("\nHi!\n")
    
    print("This is a pomodoro/time manager app!\n")
   
    print("When running the app you are able to use some arguments to modify the behavior of the program.\n")
 
    print("Those arguments are:")
    print("    -h or --help                   Get this message")
    print("    -s or --settings               Customize your personal settings (pomodoro time, number of pomodoros until a long break...)")
    print("    -r or --reset                  Reset settings \n")
    print("    -d or --data                   Dump on the console the time you have spent doing the various activities \n")
    print("    enter a number and a word      Start a new Pomodoro with n (number entered) cycles, with the time added to the database")
    print("    ex: 3 coding \n\n")

    print(signature)


def settings():
    work = input("\nTime (in minutes) for a WORK pomodoro: ")
    sb = input("\nTime (in minutes) for a SHORT break: ")
    lb = input("\nTime (in minutes) for a LONG break: ")
    ul = input("\nNumber of short breaks before a long one: ")
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            data['work'] = float(work) if work else data['work']
            data['short'] = float(sb) if sb else data['short']
            data['long'] = float(lb) if lb else data['long']
            data['untilLong'] = float(ul) if ul else data['untilLong']
            

        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    except:
        print(errorStr) 

def reset():
    with open(filename, 'r') as f:
        data = json.load(f)
        data['work'] = 25
        data['short'] = 5
        data['long'] = 10
        data['untilLong'] = 3
            
    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    delete()
    print("\nThe values were reseted!\n ")


def working(ti, t, c):
    clear()
    print("WORK!!!\n")
    playsound('./data/sfx.wav')
    for i in trange(int(ti*60),bar_format="{l_bar}%s{bar}%s" % (Fore.BLUE, Fore.RESET)):
        time.sleep(1)
        t += 1
    addTime(t, c)
        
def shortB(ti, t, c):
    clear()
    print("Short Break!\n")
    playsound('./data/sfx.wav')
    for i in trange(int(ti*60),bar_format="{l_bar}%s{bar}%s" % (Fore.GREEN, Fore.RESET)):
        time.sleep(1)
        t += 1
    addTime(t, c)

def longB(ti, t, c):
    clear()
    print("Long Break!\n")
    playsound('./data/sfx.wav')
    for i in trange(int(ti*60),bar_format="{l_bar}%s{bar}%s" % (Fore.RED, Fore.RESET)):
        time.sleep(1)
        t += 1
    addTime(t, c)

def load():
    with open(filename, 'r') as f:
        data = json.load(f)
        return [data['work'], data['short'], data['long'], data['untilLong']]

def pomodoro(l, n, t, c):
    for i in range(1, n+1):
        if i % (int(l[3])+1) == 0:
            working(l[0], t, c)
            longB(l[2], t, c)
        else:
            working(l[0], t, c)
            shortB(l[1], t, c)
    
def create(c):
    with open(db, 'r') as f:
        data = json.load(f)
        data[c] = 0
   
    os.remove(db)
    with open(db, 'w') as f:
        json.dump(data, f, indent=4)

def addTime(t, c):
    try:
        with open(db, 'r') as f:
            data = json.load(f)
            data[c] += t/60
    
        os.remove(db)
        with open(db, 'w') as f:
            json.dump(data, f, indent=4)
    except:
        create(c)
        addTime(t,c)

def d():
    with open(db, 'r') as f:
        data = json.load(f)
        for info in data:
            print(info, " -> ", data[info] )

def delete():
    os.remove(db)
    data = {}
    with open(db, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    data = load()
    t = 0
    if len(sys.argv) == 1:
        c = None
        while not c:
            c = input("What is this time for? ")
        pomodoro(data, 4, t, c)
        

    elif len(sys.argv) == 2:
        if (sys.argv[1] == "-h") or (sys.argv[1] == "--help"):
            helping()
        elif (sys.argv[1] == "-s") or (sys.argv[1] == "--settings"):
            settings()
        elif (sys.argv[1] == "-r") or (sys.argv[1] == "--reset"):
            reset()
        elif (sys.argv[1] == "-d") or (sys.argv[1] == "--data"):
            d()
        else:
            print(errorStr)
            print("\nType --help if you are having trouble.\n")
    elif len(sys.argv) == 3:
        try: 
            num = int(sys.argv[1])
            c = sys.argv[2]
            pomodoro(data, num, t, c)
            
        except:
            print(errorStr)
    else:
        print(errorStr)
        print("\nToo many arguments were given!\n")
        print("\nType --help if you are having trouble.\n")


if __name__ == "__main__":
    from tqdm import trange
    from colorama import Fore
    from playsound import playsound
    import time
    import os
    import sys
    import json
    main()
    

#TODO: add -data command