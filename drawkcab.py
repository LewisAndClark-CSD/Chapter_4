#! /usr/bin/python3
# drawkcab.py
# Luke Gosnell
# 10/27/2014

# Design:
# Ask the user to enter a message to type backwards
# Reverse the letters for the user

print("Enter message to spell backwards! ")

message = input("Message: ")
message = message[::-1]
print(message)
