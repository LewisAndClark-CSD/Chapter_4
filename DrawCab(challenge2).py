#! usr/bin/python3

# Program Name: Drawcab.py
# Author: Thomas Morrissey
# Date Written: 10-22-2014
x = input("Line: ")
y = ""
z = len(x)-1
for i in range(z, -1, -1):
    y = y +x[i]
print(y[:])
