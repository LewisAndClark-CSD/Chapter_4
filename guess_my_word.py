# guess my word
# Author: Bo Meers

import random

words = ("airplane","album","baby","banana","car","chess","dress","drum","earth")

word = random.choice(words)
correct = word
letters = []
for i in word:
    letters.append(i)
tries = 5
found = []

print(
"""                        Welcome to Guess My Word!

               Your word has " + len(word) + " letters in it.
            You have 5 tries to see what letters are in the word.
"""
)
while tries != 0:
    print("Letters Found: " + str(found))
    print("Tries Left: " + str(tries))
    letter = input("\nGuess a letter: ")
    tries -= 1

    if letter in letters:
        found.append(letter)
        
print("Letters Found: " + str(found))
guess = input("Your final guess: ")
if guess != correct:
    
    print("Sorry, that's not it.")
    
elif guess == correct:
    print("That's it!  You guessed it!\n")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
