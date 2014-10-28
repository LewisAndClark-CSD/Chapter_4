# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
HINTS = ["Its a snake....","What game is this? ","This game is either _____ or it's difficult.","This game is either easy or it's ______.","What do you do to a phone?", "Its an instrument."]
#Score
score = 0
#Tries for hints
tries = 0
playGame = False
#Ask to play the game
response = input('Do you want to play Word Jumble?(yes/no) ')
if response == 'yes':
    playGame = True


while playGame:
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
    print("The jumble is:", jumble)
    hint = ""
    guess = input("\nYour guess: ")
    while guess != correct and guess != "":
        print("Sorry, that's not it.")
        hint = input('Do you want a hint?(yes/no) ')
        if hint == 'yes':
            if correct == 'python':
                print(HINTS[0])
            elif correct == 'jumble':
                print(HINTS[1])
            elif correct == 'easy':
                print(HINTS[2])
            elif correct == 'difficult':
                print(HINTS[3])
            elif correct == 'answer':
                print(HINTS[4])
            else:
                print(HINTS[5])
        guess = input("Your guess: ")

    if guess == correct:
        print("That's it!  You guessed it!\n")
        score += 2
        if hint == 'yes':
            print('YOU USED A HINT! -1')
            score -= 1

    response = input('You have a score of '+str(score)+', do you want to play again? (yes/no) ')
    if response == 'no':
        playGame = False
input("\n\nPress the enter key to exit.")
