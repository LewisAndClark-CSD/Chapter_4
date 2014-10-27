# Counter
# Author: Bo Meers

import time

a = int(input("What number would you like me to count to? "))
b = int(input("Where would you like me to start at? "))
c = int(input("How many numbers should I count by? "))

for i in range(b, (a+1), c):
    print(i)
    time.sleep(0.5)
