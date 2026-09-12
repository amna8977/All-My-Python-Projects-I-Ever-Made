def getName():
    name = input("what is your name")
    return name


def getActivity():
    activity = input("wanna play a game or go outside ")
    return activity



answer = "yes"

while answer == "yes": 
    name = getName()
    print("hello," +name+".")

    activity = getActivity()
    if activity ==  "game":
       print ("Lets game")
       answer = input("play again?")

    if activity ==  "outside" :
        print ("Lets play tag")
        answer = input("play again?")

