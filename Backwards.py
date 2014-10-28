#Backwards.py
#By: Karlos Calvillo
#10/22/14

print("Hello! Lets type a word backwards for you.")

message=input("Type a word: ")
backward=""
counter=len(message)

while counter !=0:
    backward+=message[counter-1]
    counter-=1
print(backward)
