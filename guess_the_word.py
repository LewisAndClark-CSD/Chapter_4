import random

print("Welcome to GUESS THE WORD!!!")

WORDS = ("halloween", "pumpkin", "skeleton", "ghost", "vampire", "zombie")

word = random.choice(WORDS)

correct = word

letters1 = "This word has 9 letters."
letters2 = "This word has 7 letters."
letters3 = "This word has 8 letters."
letters4 = "This word has 5 letters."
letters5 = "This word has 7 letters."
letters6 = "This word has 6 letters."

if correct == WORDS(0):
    print(letters1)
elif correct == WORDS(1):
    print(letters2)
elif correct == WORDS(2):
    print(letters3)
elif correct == WORDS(3):
    print(letters4)
elif correct == WORDS(4):
    print(letters5)
elif correct == WORDS(5):
    print(letters6)

guesses = 5
    
letter_guess = input("Guess a letter: ")
if letter_guess in word:
    print("Great Job! That's in the word!")
    return(letter_guess)
    guesses += 1
else:
    print("Sorry, that's not in the word.")
    return(letter_guess)
    guesses += 1
    
if guesses += guesses:
   word.guess = input("What's the secret word? ")
   
if word.guess == correct:
  print("Congratulations! You got the answer right! The word was,", word)
  print("Thanks for playing my little game.")
if word.guess !== correct:
  print("Oh, I'm sorry, the correct answer was", word)
  print("Please try again, if you want to.")
  
 input("\n\nPress the enter key to exit.")
    
