#numberCount.py
#By: Karlos Calvillo
#10/22/14

print("Hello! Let me count for you.")

startNumber=int(input("Enter starting number: "))
endNumber=int(input("Enter end number: "))
interval=int(input("Which amount should I count by?: "))

print("Counting:")
for i in range(startNumber, endNumber+1, interval):
    print (i)
