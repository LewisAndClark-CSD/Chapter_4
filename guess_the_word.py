#! /usr/bin/python3
# guess_the_word.py
# Luke Gosnell
# 10/27/2014

# Design:
# Tell the user how to play the game
# Pick a random word and ask the user to guess letters in the word
# After five tries, tell the user to guess the word
# Tell the user whether or not they guessed correctly

import random

WORDS = ['hopscotch', 'deviant', 'decadence', 'weenies', 'cola', 'slow', 'farmer', 'dragon']

print("I'm thinking of a word...")
word = random.choice(WORDS)
guess = 0
correct = 0
again = True
answer = ""

print("""
                             GUESS THE WORD!!!
I will pick a arndom word and will tell you how many latters are in the word.
You will try to guesswhat letters are in the word,
and after five chances, you must guess the word! """)
print(" ")

print("The word has " + str(len(word)) + " letters!")
print(" ")

while again:
    answer = input("Guess a letter: ")
    guess = guess + 1
    for Letter in word:
        if answer == Letter:
            correct = correct + 1
    if correct == 0:
        print("Nope!")
    else:
        print("Yep, that is a correct letter!")
        correct = 0
    if guess == 5:
        again = False
print(" ")
final = input("No more guesses! What's the word? ")

if final == word:
    print(" ")
    print("That's right!!! YAY!")
else:
    print("Sorry, that's not the word....... Loser")
    
