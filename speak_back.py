# Speaking Backwards
# Author: Bo Meers

a = input("Line: ")
backWord = ""
b = len(a)-1
for i in range(b, -1, -1):
  backWord = backWord + a[i]
print(backWord[:])
