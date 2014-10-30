# Word Jumble
# Latest Author: Alton Stillwell (10/24/14)
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# other variables
hadHint = False
tries = 0
temp = ''
points = 10
# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""
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
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    tries = tries + 1
    print("Sorry, that's not it.")
    if hadHint == True:
        if correct == 'python':
            print("Hint: 'sssss'")
        elif correct == 'jumple':
            print("Hint: 'nage'")
        elif correct == 'easy':
            print("Hint: 'peasy'")
        elif correct == 'difficult':
            print("Hint: 'hard'")
        elif correct == 'answer':
            print("Hint: 'question'")
        elif correct == 'xylophone':
            print("Hint: 'instrument'")
        else:
            print("Error")
    guess = input("Your guess: ")
    if tries == 5:
        temp = input("You seem to be stuck, would you like a hint(yes/no): ")
        if temp == 'yes':
            hadHint = True
    
if guess == correct:
    print("That's it!  You guessed it!\n")

print("Thanks for playing.")
if hadHint == True:
    print("You earned:", points - 5 - tries,"points.")
else:
    print("You earned:", points - tries,"points.")
input("\n\nPress the enter key to exit.")
