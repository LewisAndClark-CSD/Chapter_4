# guess_the_word.py
# Author: Sam Coon
# Date: 10/24/14

import random

words = ["pickle","dog","star","impossible","backpack"]
count = 5

print("\t\t\tWelcome to guess the word!")
print("\tYou will be given the amount of letters in the word and then\n\tfive times to guess what letters are in the word.")
rand = random.choice(words)
print("\nThe word has",(len(rand)),"letters")
print(rand)

while count > 0:
    guess = input("Guess a letter in the word: ")
    count = count - 1
    if guess in rand:
        rand.index(guess)
        print("Guess is correct!")
    else:
        print("Nope try again.")
if count == 0:
    guessWord = input("Now guess the word: ")
if guessWord == rand:
    print("You got it!")
else:
    print("Sorry that's not it!")


print("\nThanks for playing!")
input("\nPress enter to exit: ")

    
