#! /usr/bin/python3
# count.py
# Luke Gosnell
# 10/27/2014

# Design:
# Ask the user to enter a starting number
# Ask the user to enter an ending number
# Ask the user to enter a number to count by
# Count by the entered number from the starting number to the ending number

startNumber = int(input("Enter starting number: "))
endNumber = int(input("Enter end number: "))
countNumber = int(input("Enter number to count by: "))

for i in range(startNumber, endNumber, countNumber):
    print(i)
print(endNumber)
