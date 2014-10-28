#word_jumble_two.py
#By: Karlos Calvillo
#10/27/14

# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word

hint0 = "It's a type of snake"

hint1 = "It's what this program does to words to make it difficult"

hint2 = "Not difficult but.."

hint3 = "This is not easy"

hint4 = "With every question there's a.."

hint5 = "It's a musical instrument you have to hit with 2 small sticks"


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
(Press the enter key at the prompt to quit.
If you don't use any hints you get points!)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
guess=guess.lower()
score=0
while guess != correct and guess != "":
    print("Sorry, that's not it.")

    hintPrompt=input("Would you like a hint? Y/N: ")

    if hintPrompt=="Y" and correct==WORDS[0]:
        print(hint0)

    elif hintPrompt=="Y" and correct==WORDS[1]:
        print(hint1)

    elif hintPrompt=="Y" and correct==WORDS[2]:
       print(hint2)

    elif hintPrompt=="Y" and correct==WORDS[3]:
        print(hint3)

    elif hintPrompt=="Y" and correct==WORDS[4]:
        print(hint4)

    elif hintPrompt=="Y" and correct==WORDS[5]:
        print(hint5)

    elif hintPrompt=="N":
        score+=50

    guess = input("\nYour guess: ")
    guess=guess.lower()
    
if guess == correct:
    print("That's it!  You guessed it!\n")
    print("You got: "+str(score)+" points")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
