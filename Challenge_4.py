#Challenge_4
#Dennis Gordick
#10/23/2014
import random
WORDS=["airport","bathroom","carrot","drum","electricity","festival","gemstone","horoscope","insect","junk","kitchen","library","microscope","necklace","onion","parachute","rainbow","sandpaper","television","umbrella","vampire","water"]
play=input("Do you want to play? (yes or no)")
while play=="yes":
    word= random.choice(WORDS)
    correct = word
    number=len(correct)
    count=0
    print("The number of letters in the word is "+str(number))
    while int(count)<5:
        letter=input("Guess a letter, and i will tell you if that letter is in the word by saying yes or no.")
        if letter in correct:
            print("Yes")
        else:
            print("No")
        count+=1
    print("You get as many guesses you want... But im keeping track of the total guesses. You can always leave it black to quit")
    guess_count=1
    guess=input("Your guess?")
    while guess != correct and guess !="":
        print("That is wrong...")
        guess=input("Guess again.")
        guess_count+=1

    if guess == correct:
        print("That is correct! You guessed it, now prepare to die!")
        print("Your total guesses: "+str(guess_count))
    elif guess=="":
        print("You quit. You are a discrase.")

    play=input("Do you want to play again? (yes or no)")

print("Thanks for playing. Now get out of my sight!")
