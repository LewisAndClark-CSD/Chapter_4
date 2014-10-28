#wordGuess.py
#By: Karlos Calvillo
#10/27/14

import random

tries=7
WORDS=("Link", "Epona", "Zelda", "Ganondorf", "Navi", "Midna")
count=1

answer=random.choice(WORDS)
print("Welcome to Word Guess! This word guess is Zelda themed!")
print("Enjoy!")
    
print("There are", len(answer), "Letters in the word")

letters=input("What letters are in the word?: ")

while tries != 2:

    if letters in answer:
        print("Yes")
        letters=input("What letter do you guess?")
        tries=tries-1

    else:
        print("No")
        letters=input("What letter do you guess?")
        tries=tries-1
print("Time to have a guess")

guess=input("What is the word?: ")

while guess != answer:
    print("That is incorrect, try again.")
    guess=input("What is the word?: ")


if guess==answer:
    print("Good job! That is correct.")
    print("I hope you enjoyed the game!")
