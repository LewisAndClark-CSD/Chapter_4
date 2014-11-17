#Challenge 1 
#Author: Jose Chica

sNumber = int(input('What number would you like to start at: '))
eNumber = int(input('What number would you like to end at: '))
aNumber = int(input('What amount would you like it to be counted by: '))

for i in range(sNumber, eNumber, aNumber):
    print(i, end=" ")

input("\n\nPress the enter key to exit.\n")
