#Backwards.py
#Karl Pearson
#10/27/2014
message=input('Type a word to spell backwards: ')
backward=""
counter=len(message)
while counter !=0:
    backward+=message[counter-1]
    counter-=1
print(backward)
