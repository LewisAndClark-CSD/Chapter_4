# Counter

start = int(input("Choose a starting number: "))
end = int(input("Choose an ending number: "))
bywhat = int(input("Count by what? "))

print("Now Counting...")
for i in range(start, end, bywhat):
    print(i, end=" ")
