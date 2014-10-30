# Chapter 4 challenge 4
# Author: Alton Stillwell
# Date: 10/27/14
#########################
# Design
# computer picks a random word from a list('WORD'), sets to 'correct'
# print number of letters in the word
# have user guess which letter('guess')
# respond with 'yes' or 'no'
# print progress
# user is limited to five guesses for the letters,
# then has 1 chance to guess the word
##################################################
# preliminary variables
import random
count = 0
times = 0
letterList = []
WORD = ("squirell","wombat","train","elephant","world","zebra")
# flavor text
print("\t\nWelcome to Alton's Amazing Word Guessing Game, 2015 Edition!")
print("\nIn the game, you will be prompted to guess a letter for a word")
print("that the computer has chosen at random..")
print("\nYou will get 5 guesses for letters, and then will be asked")
print("for the word. You only get one shot, so good luck!\n")
print("Also be sure to only use lowercase letters!\n")
# chose word
correct = random.choice(WORD)
for i in correct:
    count = count + 1
    letterList.append(i)
print("Your word contains",count,"letters.")
guess = input("Guess a letter: ")
times = times + 1
while times < 5:
    if guess in letterList:
        print(guess,"is in the word!")
    else:
        print(guess,"is not in the word!")
    times = times + 1
    guess = input("Guess a letter: ")
# ending output
lastChance = input("Enter what you think the word is: ")
if lastChance == correct:
    print("YOU DID IT! THE WORD WAS INDEED", correct)
else:
    print("Sorry, that was not the right word..")
    print("The correct word was: " + correct)

