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

#create hints for jumbled words
hint0 = "\nIt's an efficient and best programming language for a beginner to start at...\n"
hint1 = "\nIt's what this program does to words for the user (you) to guess them...\n"
hint2 = "\nIf a program isn't difficult, it's..."
hint3 = "\nIf a program isn't easy, it's..."
hint4 = "\nYou have a question. You get the...\n"
hint5 = "\nA musical instrument played with 2 sticks which you hit against it...\n"

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

guess = input("\nYour guess: ")
guess = guess.lower()
score = 0
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    needhint = input("Would you like a hint? Yes/No: ")
    needhint = needhint.lower()
    if needhint == "yes" and correct == WORDS(0):
      print(hint0)
    elif needhint == "yes" and correct == WORDS(1):
      print(hint1)
    elif needhint == "yes" and correct == WORDS(2):
      print(hint2)
    elif needhint == "yes" and correct == WORDS(3):
      print(hint3)
    elif needhint == "yes" and correct == WORDS(4):
      print(hint4)
    elif needhint == "yes" and correct == WORDS(5):
      print(hint5)
    elif needhint == "no":
      score += 50
      
    guess = input("Your guess: ")
    guess = guess.lower()
    
if guess == correct and needhint == "no":
    print("That's it!  You guessed it!\n")
    print("Since you didn't want a hint you recieved", score, "points! Congratulations!\n"

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
