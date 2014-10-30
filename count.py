# Chapter 4, Challenge 1
# Author: Alton Stillwell
# Date: 10-24-14
#########################
# input
sNum = int(input("Enter a starting number: "))
eNum = int(input("Enter an ending number: "))
step = int(input("Enter step size: "))
# loop
print(sNum)
while sNum != eNum:
    sNum = (sNum + step)
    print(sNum)

