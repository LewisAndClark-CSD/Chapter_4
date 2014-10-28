#! /usr/bin/python3
# word_jumble.py
# Luke Gosnell
# 10/27/2014

# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word
amount = 0

#Hints
if word == "python":
    hint = "Computer program"
elif word == "jumble":
    hint = "I just did it to these words"
elif word == "easy":
    hint = "This game is pretty _ _ _ _"
elif word == "difficult":
    hint = "This game isn't very _ _ _ _ _ _ _ _ _"
elif word == "answer":
    hint = "Opposite of problem"
elif word == "xylophone":
    hint = "Musical instrument"

# create a jumbled version of the word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
""")

print("The jumble is:", jumble)
reward = ""

guess = input("\nYour guess: ")
while (guess != correct and guess != ''):
    print("Sorry, thats not it.")
    response = input("Would you like a hint? (y/n) ")
    if response == "y":
        amount = amount + 1
        print(hint)
    
        
    
    guess = input("Your guess: ")
    
if guess == correct:
    print("That's it!  You guessed it!\n")

    if amount == 0:
        print("You solved it without a hint! Good job!")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
