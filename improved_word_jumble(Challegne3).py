# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random
NoHelp = 0
hint = ""
Help = ""
# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word
if word == "Python":
    hint = "It is a programming language."
elif word == "jumble":
    hint = "It is another word for a mess."
elif word == "easy":
    hint =  "It's another word for not difficult."
elif word == "difficult":
    hint = "It's another word for not east."
elif word == "answer":
    hint = "It's the opposite of a riddle."
elif word == "xylophone":
    hint = "It's is an wooden instrument."

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
    print("Sorry, that's not it.")
    Help = input("Would you like a hint?(Yes or No) ")
    if Help == "Yes":
        NoHelp = NoHelp + 1
        print(hint)
    elif Help == "No":
        print()
    else:
        print("Sorry, I don't follow.")
    guess = input("Your guess: ")
    
if guess == correct:
    print("That's it!  You guessed it!\n")
if NoHelp == 0:
    print("You solved it like a true camp! Congrats!!!!")
else:
    print("Try not to ask for a hint next time.")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
