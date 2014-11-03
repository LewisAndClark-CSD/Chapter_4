# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
HINTS = ("snake", "mixed", "simple", "hard", "final ____", "ding ding ding")

# pick one word randomly from the sequence
word = random.choice(WORDS)

wordPlace = WORDS.index(word)

# create a variable to use later to see if the guess is correct
correct = word

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
"""
)

bonusPoints = 0

print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    hint = input("Would you like a hint(Y/N)? ")
    if hint.lower() == "y":
        print(HINTS[wordPlace])
        guess = input("\nYour guess: ")
    if hint.lower() == "n":
        bonusPoints += 1
        guess = input("\nYour guess: ")
if guess == correct:
    print("That's it!  You guessed it!\n")
    print("You recieved %d bonus points" % bonusPoints)
print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
