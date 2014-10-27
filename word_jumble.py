# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

word = random.choice(WORDS)

correct = word

jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)


guess = input("\nYou can either guess the word or get a (H)int: ")
while guess != correct and guess != "":
    
    if guess in ("H","h"):
        
        if correct == "python":
            guess = input("It's a type of snake.")
            
        elif correct == "jumble":
            guess = input("It's what i'm doing to these words.")

        elif correct == "easy":
            guess = input("The opposite of hard.")

        elif correct == "difficult":
            guess = input("The opposite of easy.")

        elif correct == "answer":
            guess = input("You are trying to figure out the ______.")

        elif correct == "xylophone":
            guess = input("You can find this in a music store.")
            
    else:
        print("Sorry, that's not it.")
        guess = input("\nYou can either guess the word or get a (H)int: ")
        
    
if guess == correct:
    print("That's it!  You guessed it!\n")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
