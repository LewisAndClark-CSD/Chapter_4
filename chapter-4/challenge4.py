import random


WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

word = random.choice(WORDS)

wordLength = len(word)

print("There are %d letters in the word" % wordLength)

goodGuess = []

for i in range(5):
    guess = input("Guess one of the letters in the word: ")

    if guess.lower() in word:
        print("Yes")
        goodGuess.append(guess)
    else:
        print("No")
print("Letters in the word:", goodGuess)
wordGuess = input("Guess the whole word: ")

if wordGuess == word:
    print("You guessed it!")

else:
    print("Incorrect")
    wordGuess = input("Guess hte whole word: ")