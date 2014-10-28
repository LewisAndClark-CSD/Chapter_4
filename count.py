# count.py
# Author: Sam Coon
# Date: 10/23/14

print("Counting program")
start = int(input("\nEnter the number you want to start at: "))
end = int(input("Enter the number you want to end at: "))
skip = int(input("Enter the amount you want to count by: "))

for i in range(start,end + skip,skip):
    if i <= end:
        print(i)
    
   
