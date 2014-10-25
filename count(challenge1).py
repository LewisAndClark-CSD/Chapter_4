#! bin/usr/python#
# Program Name: Count.py
# Date Written: 10-21-2014
# Author: Thomas Morrissey
print("""
    Welcome to Count!
  Today, You will tell me what number
  to begin with, to end with and what
  number to count by(like 2,4,6,8,10,
  etc.)
""")
StartNumber=int(input("What number do you wish to beign with? "))
EndNumber=int(input("What is the ending number? "))
MultpleNumber=int(input("What is number to count by? "))
for i in range(StartNumber, EndNumber, MultpleNumber):
    print(i)
print(EndNumber)
  
