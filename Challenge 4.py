#Challenge 4

#imports
import random

#Values
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
playGame = False
tries = 5
guess = ''

#Start the game
response = input('Do you want to play the guessing game? ')
if response == 'yes':
    playGame = True

while playGame:
    word = random.choice(WORDS)
    print('\nThe word has '+str(len(word))+' letters.')
    while tries != 0:
        print('\nGuess a letter (or phrase) that is in the word!')
        check = input('You have '+str(tries)+' guesses left: ')
        tries -= 1
        if check == word:
            playGame = False
            guess = word
            tries = 0
            print('WOW YOU GUESSED IT ALREADY')
        if check in word:
            print('\nYes! That is in the word.')
        else:
            print('\nNo, sorry that letter is not in the word')
    while guess != word:
        guess = input('Guess the word: ')
        if guess != word:
            print('\nSorry! Try again!')
    playGame = False

print('Good job you guessed the word!')
input('\nPress <enter> to exit')
