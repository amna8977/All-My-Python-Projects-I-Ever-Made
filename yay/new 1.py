import datetime
now = datetime.datetime.now()

if now.hour < 12:
    greeting = "I hope this morning gave you no reason to have a crashout"
elif now.hour < 13:
    greeting = "hey chat. did u get a good afternoon"

else:
    greeting = "yo,dude. good evening"


name = input("What's your name? ")

print(f"{greeting}, {name}! Welcome!")

