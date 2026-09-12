# Import library so we can use at random
import random 

# ask user for their name
name=input("what is your name?")

#say hello to the user
print("Yo,"+name+", nice to meet you")

# get random number from the computer
rand = random.randint(1,100)


#assign "guess" a default number
guess = 3


while  guess != rand:

# Ask user to guess a number
    guess= int(input("what number am i thinking of? "))

# check if number is correct
    if guess == rand: 
        print("you were right")

    if guess < rand:
        print ("too low!")
        
    if guess > rand:
        print("too big")
