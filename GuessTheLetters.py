#GuessTheWord.py
#Karl Pearson
#10/27/2014
import random

print("Welcome to Guess the Word: Legend of Zelda Edition")
print("You will have 5 tries to guess the word")

tries=7
WORDS=("Link","Hyrule","Zelda","Epona","Ocarina","Triforce")
count=1

answer=random.choice(WORDS)

print("The word has", len(answer),"letters in the word.")

letters=input('Enter a letter: ')
while tries != 2:
        if letters in answer:
            print("Yes")
            letters=input('What letters do you guess? ')
            tries=tries-1
        else:
            print('No')
            letters=input('What letter do you guess? ')
            tries=tries-1
print("Time to have a guess")
guess=input("What is the word? ")
while guess != answer:
    print("That is incorrect, try again")
    guess=input("What is the word?: ")

if guess==answer:
    print('Good Job!')
    print('Hope you enjoyed the game')

input('\n\npress enter to exit')

