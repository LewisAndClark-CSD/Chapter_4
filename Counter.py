#Counter.py
#Karl Pearson
#10/27/2014
startNumber=int(input('Enter starting number: '))
endingNumber=int(input('Enter ending number: '))
countBy=int(input('Enter number to count by: '))
for i in range(startNumber,endingNumber+1,countBy):
    print(i)
