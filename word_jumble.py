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
score = 100
print("The jumble is:", jumble)

guess = input("\nYour guess: ")

if guess == correct:
    print("Wow you got it without a hint!")
elif guess == "":
    print("No guess?")
elif guess == "hint":
    score = score - 5
    if correct == "python":
        print("It's a kind of snake.")
        input("Your guess: ")
        score = score - 1
    elif correct == "jumble":
        print("Welcome to Word _____!")
        input("Your guess: ")
        score = score - 1
    elif correct == "easy":
        print("The opposite of hard.")
        input("Your guess: ")
        score = score - 1
    elif correct == "difficult":
        print("This word jumble is....")
        input("Your guess: ")
        score = score - 1
    elif correct == "answer":
        print("If someone ask a question you would _____ it.")
        input("Your guess: ")
        score = score - 1
    elif correct == "xylophone":
        print("An instrament that starts with x")
        input("Your guess: ")
        score = score - 1

print("That's it you got it!")
print("Thanks for playing!")
print("Your score was",score,"out of 100!")
