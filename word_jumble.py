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

hint0 = "\nType of snake and programming language..."

hint1 = "\nmixture of letters that make a word...."

hint2 = "\nSynonym for simple..."

hint3 = "\nSynonym for hard..."

hint4 = "\nIt's not a question..."

hint5 = "\nmusicle instrument starting with 'x'..."


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
   50=Perfect Score(no hints)
   0=Okay Score(hints used)
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
guess=guess.lower()
score=0
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    hintPrompt= input("Would you like a hint? y/n: ")
    if hintPrompt == "y" and correct == WORDS[0]:
        print(hint0)

    elif hintPrompt == "y" and correct == WORDS[1]:
        print(hint1)

    elif hintPrompt == "y" and correct == WORDS[2]:
        print(hint2)

    elif hintPrompt == "y" and correct == WORDS[3]:
        print(hint3)

    elif hintPrompt == "y" and correct == WORDS[4]:
        print(hint4)

    elif hintPrompt == "y" and correct == WORDS[5]:
        print(hint5)
    elif hintPrompt == "n":
        score+=50
    guess=input("\nYour guess: ")
    guess=guess.lower()
if guess == correct:
    print("That's it!  You guessed it!\n")
    print("You got: "+str(score)+" points")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
