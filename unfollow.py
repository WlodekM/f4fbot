




import requests.exceptions
import scratchclient

import json


print("   _____                 __       __       ________ __  ______   __          __ ")
print("  / ___/______________ _/ /______/ /_     / ____/ // / / ____/  / /_  ____  / /_")
print("  \__ \/ ___/ ___/ __ `/ __/ ___/ __ \   / /_  / // /_/ /_     / __ \/ __ \/ __/")
print(" ___/ / /__/ /  / /_/ / /_/ /__/ / / /  / __/ /__  __/ __/    / /_/ / /_/ / /_  ")
print("/____/\___/_/   \__,_/\__/\___/_/ /_/  /_/      /_/ /_/      /_.___/\____/\__/  ")

print("--------------------------------------------------------------------------------")
print("You must be following at least one user who has at least a few followers to use this.")
print("I don't take responsiblity if you get banned for using this.")
print("╔╦╗╦ ╦╦╔═╗  ╦╔═╗  ╔╦╗╦ ╦╔═╗  ╦ ╦╔╗╔╔═╗╔═╗╦  ╦  ╔═╗╦ ╦  ╔╗ ╔═╗╔╦╗")
print(" ║ ╠═╣║╚═╗  ║╚═╗   ║ ╠═╣║╣   ║ ║║║║╠╣ ║ ║║  ║  ║ ║║║║  ╠╩╗║ ║ ║ ")
print(" ╩ ╩ ╩╩╚═╝  ╩╚═╝   ╩ ╩ ╩╚═╝  ╚═╝╝╚╝╚  ╚═╝╩═╝╩═╝╚═╝╚╩╝  ╚═╝╚═╝ ╩ ")
vartimeinterval = 1
times = 1

def start(фм):
    
    config = open("C:\ScratchF4FBot-master\config.json", "r")
    import math
    config_loaded = json.loads(config.read())

    times = int(config_loaded["times"])
    

    i = 0
    
    username = config_loaded["userName"]
    password = config_loaded["password"]

    #def settings(c):

    times = int(input("How many people to unfollow? "))

    vartimeinterval = float(input("Wait: "))
    userpass = input("Use username and password from config.json? ")
    userpass = userpass.lower()

    if userpass == "n" or userpass == "no" or userpass == "false" or userpass == "f":
        username = input("Username: ")
        password = input("Password: ")
        pass
    #    pass
        
    #settings

    #command = input(">")

    #while not command == start:
    #    command = input(">")
    #    if command == "help" or command == "hlp":
    #        print("")
    #        print("help - Get the command info")
    #        print("start - Start the program")
    #        print("settings - edit settings")
    #        pass
    #
    #
    #    pass
    #word = str(0)
    #sort = input("Sort? ")
    #sort = sort.lower()
    #if sort == "y" or sort == "yes" or sort == "true" or sort == "t":
    #    word = input("Sort by word: ")
    #    word = word.lower()
    #    pass

    session = scratchclient.ScratchSession(username, password)

    dtimes = times
    times = times - 1
    import time

    past = time.time()
    prev = time.time()

    while i <= times:
        following = session.get_user(username).get_following()

        for f in following:
            if i <= times:
                try:
                
                                        seconds = time.time() - past
                                        seconds = math.floor(seconds)
                                        t = seconds
                                        ts = t % 60
                                        tm = (t - ts) / 60
                                        tm = math.floor(tm)
                                        i = i + 1
                                        tsstr = str(ts)
                                        tmstr = str(tm)
                                        ttook = time.time() - prev

                                        ttook = round(ttook *1000) / 1000

                                        print(i,"/",dtimes)
                                        print("Unollowed", f.username)
                                        print("Time:", tsstr + "s", tmstr + "m")
                                        print("Time taken:", ttook)
                                        print()
                                        prev = time.time()

                                        #Follow the user
                                        f.unfollow()
                                        #Wait timeInterval from cofig seconds
                                        time.sleep(vartimeinterval)
                
                except requests.exceptions.JSONDecodeError:
                    pass
                pass
                                
                                

    print("end")

    again = input("Run again? ")
    again = again.lower()
    if again == "y" or again == "yes" or again == "true" or again == "t":

        n = 10

        for i in range(n):
            print()
            print()
            print()
            pass

        start("starting...")

    pass
start("starting")

