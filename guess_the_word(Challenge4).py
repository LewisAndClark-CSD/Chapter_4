#! usr.bin/python3
# Program Name: Guesst_the_Word.py
# Author: Thomas Morrissey
# Date Written: 10-25-3014
import random
WORDS = ['python', 'easy', 'difficult', 'programming', 'computers']
word = random.choice(WORDS)
guess = 0
correct = 0
again = True
Answer = ""
print("""
    ===Welcom to Guess The Word!===
Here's how the game works! I will pick the word from
random, I will tell you how many letter are in the word,
and you will try to guess what it is. You have five chances
to guess what letters are in the word, I can not tell you where with in the
word that letter is nor how many times it appears. After the five guesses
you will have one chance to guess what the word is.""")
Continue=input("Do you wish to play?(Yes or No) ")
if Continue == "No":
    print("Goodbye.")
    exit()
print("This word in particular has "+str(len(word)))
while again:
    Answer=input("What letter is in the word? ")
    guess=guess+1
    for Letter in word:
        if Answer == Letter:
          correct = correct+1
    if correct==0:
        print("Sorry, "+Answer+" is not in the word.")
    else:
        print("Yes, "+Answer+" is in the word.")
        correct= 0
    if guess == 5:
        again = False
Result = input("What is the word? ")
if Result == word:
    print("Holy cow! You got it!")
    print("The word is "+word+".")
else:
    print("I'm sorry. You didn't get the word.")
    print("The word is "+word)
print("Thanks for playing.")

    
