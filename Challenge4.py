# Challenge 4
#Author: Jose Chica

import random

WORDS = ("Eminem", "bow", "Tom", "lunch box", "chimichanga")
word = random.choice(WORDS)
Correct = word
guess = " "

a=input("Hello my friend would you like to guess what word I'm thinking of?(y/n) ")
if a== "y":
    print("""Alright mate.
The rules are simple. I describe what it is and you tell me what you think it
is. You get 5 chances on guessing what letters it has. Then you guess what it
is. Lets begin.""")

    if word == "Eminem":
        print("This is a man who made a song called Rap God.")
    elif word == "bow":
        print("This object is very silent when you shoot it.")
    elif word == "Tom":
        print("He is praised in the CIS room. He is also Luke's lover.")
    elif word == "lunch box":
        print("This object can hold your food.")
    elif word == "chimichanga":
        print("This is something Jose makes at work. Also, its Deadpool's favorite food.")
    tries = 0
    correct = 0
    while tries != 5:
        question = input("What letter are you thinking? ")
        for i in word:
            if i == question:
                correct = correct+1
        tries = tries+1

        if correct == 0:
            print('no')
        else:
            print("YES!")
            correct = 0
    while guess != Correct:
        guess = input("What do you think it is mate? ")
        if guess != Correct:
            print("Im sorry its wrong my friend.")
    print("Nice mate, you found out what I was thinking.")
if a== "n":
    print("Ok. Maybe next time friend.")
    
