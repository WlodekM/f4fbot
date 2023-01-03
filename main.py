




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


def start(фм):
    print(фм)
    config = open("C:\ScratchF4FBot-master\config.json", "r")
    import math
    config_loaded = json.loads(config.read())

    times = int(config_loaded["times"])
    


    i = 0
    vartimeinterval = config_loaded["timeInterval"]
    username = config_loaded["userName"]
    password = config_loaded["password"]

    setupmanual = input("Run w/ settings from config.json? ")
    setupmanual = setupmanual.lower()

    if setupmanual == "n" or setupmanual == "no" or setupmanual == "false" or setupmanual == "f":

        times = int(round ( float ( input("How many people to follow: ") ) ) )
        vartimeinterval = float(input("Time interval:") )
        userpass = input("Use username and password from config.json? ")
        userpass = userpass.lower()

        if userpass == "n" or userpass == "no" or userpass == "false" or userpass == "f":
            username = input("Username: ")
            password = input("Password: ")
            pass

        pass
    
    session = scratchclient.ScratchSession(username, password)

    dtimes = times
    times = times - 1
    import time

    past = time.time()

    while i <= times:
        following = session.get_user(config_loaded["userName"]).get_following()

        for f in following:
        
            try:
                #Get followers of f
                gotten = f.get_followers()

                if len(gotten) > 0 and i <= times:

                    for g in gotten:

                        if not g.username == config_loaded["userName"] and i <= times:

                            #Time calculations
                            seconds = time.time() - past
                            seconds = math.floor(seconds)
                            t = seconds
                            ts = t % 60
                            tm = (t - ts) / 60
                            tm = math.floor(tm)
                            i = i + 1
                            tsstr = str(ts)
                            tmstr = str(tm)
                            
                            print(i,"/",dtimes)
                            print("Followed", g.username)
                            print("Time:", tsstr + "s", tmstr + "m")
                            print()

                            #Follow the user
                            g.follow()
                            #Wait timeInterval from cofig seconds
                            time.sleep(vartimeinterval)
            #error
            except requests.exceptions.JSONDecodeError:
                pass
    print("end")

    again = input("Run again? ")
    again = again.lower()
    if again == "y" or again == "yes" or again == "true" or again == "t":

        start("starting")

    pass
start("starting")

