# Chapter 4, Challenge 2
# Author: Alton Stillwell
# Date: 10-24-14
#########################
# variables
message = input("Enter message: ")
count = 1
egassem = ""
# Loop
for i in range(len(message)):
    egassem += message[-(count)]
    count += 1
# Output
print(egassem)
