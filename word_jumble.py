# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")


print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)


play=input("Do you want to play? (yes or no)")
while play=="yes":
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

    print("The jumble is:", jumble)
    points=100
    guess = input("\nYour guess: ")
    while guess != correct and guess != "":
        print("Sorry, that's not it.")
        hint=input("Do you need a hint?")
        if hint=="yes":
            points=int(points)-10
            if correct=="python":
                print("Its a snake...")
            elif correct=="jumble":
                print("Rhymes with rumble")
            elif correct== "easy":
                print("This one is so simple!")
            elif correct=="difficult":
                print("This is a hard one... its very ________________")
            elif correct=="answer":
                print("You cant find it? the _________ is ___________")
            elif correct=="xylophone":
                print("It is a toy...")
            print("Thanks for takeing the hint, idiot...")
        guess = input("Your guess: ")
        
    if guess == correct:
        print("That's it!  You guessed it!\n")
        print("Your score is: "+str(points))
        play=input("Do you want to play again? (yes or no)")
    elif guess== "":
        print("You failed...")
        play=input("Do you want to play again? (yes or no)")
    

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
