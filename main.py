import scratchclient,json,math,time,requests.exceptions,pathlib,os
title="""   _____                 __       __       ________ __  ______   __          __
  / ___/______________ _/ /______/ /_     / ____/ // / / ____/  / /_  ____  / /_
  \__ \/ ___/ ___/ __ `/ __/ ___/ __ \   / /_  / // /_/ /_     / __ \/ __ \/ __/
 ___/ / /__/ /  / /_/ / /_/ /__/ / / /  / __/ /__  __/ __/    / /_/ / /_/ / /_ 
/____/\___/_/   \__,_/\__/\___/_/ /_/  /_/      /_/ /_/      /_.___/\____/\__/

--------------------------------------------------------------------------------
You must be following at least one user who has at least a few followers to use this.
I don't take responsiblity if you get banned for using this."""

def start():
    print("Starting...")
    cnfig = pathlib.Path(__file__).parent.resolve()
    cnfig = str(cnfig)+"\config.json"
    cnfig = os.path.normpath(cnfig)
    print("Config:",cnfig)
    try:
    
        config = open(cnfig, "r")
        config_loaded = json.loads(config.read())
    
    except:

        print("Config.json not found. Put it in the folder with main.py")
        cnfig = os.path.normpath(input("Path to config.json:"))
        config = open(cnfig, "r")
        config_loaded = json.loads(config.read())

        pass

    times = int(config_loaded["times"])

    i = 0
    vartimeinterval = config_loaded["timeInterval"]
    username = config_loaded["userName"]
    password = config_loaded["password"]

    if input("Run w/ settings from config.json? ").lower() in ("n","no","false","f"):
        times = int(round ( float ( input("How many people to follow: ") ) ) )
        vartimeinterval = float(input("Time interval:") )
        userpass = input("Use username and password from config.json? ")
        userpass = userpass.lower()

        if userpass in ("n","no","false","f"):
            username = input("Username: ")
            password = input("Password: ")
            pass

        pass

    session = scratchclient.ScratchSession(username, password)

    dtimes = times
    times = times - 1

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
                            #Wait timeInterval from config seconds
                            time.sleep(vartimeinterval)
            except requests.exceptions.JSONDecodeError: # An exception
                pass
    print("End.")
    again = input("Run again? ")
    again = again.lower()
    if again ("y","yes","true","t"):
        start()
    pass
start()
