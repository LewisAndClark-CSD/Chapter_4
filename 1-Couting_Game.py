#Counting Game

#imports
import time

#starting variables
startCo = ""
endCo = ""
inco = ""
times = 0
remainder = ""
askCount = input('Do you want me to count something for you? ')

#only able to enter those inputs
while askCount.lower() not in ('yes', 'y', 'no', 'n'):
    print('Enter yes or no!')
    askCount = input('Do you want me to count something for you? ')
    
#Start or don't start counting 
if (askCount.lower() == 'yes') or (askCount.lower() == 'y'):
    starCo = True
if (askCount.lower() == 'no') or (askCount.lower() == 'n'):
    starCo = False


#Counting loop
while starCo:
    while True:
        try:    
            coFrom = int(input('Where would you like to start counting from? '))
            break
        except ValueError:
            print('Enter a valid input')
    while True:
        try:    
            endCo = int(input('Where would you like for me to stop counting? '))
            break
        except ValueError:
            print('Enter a valid input')
    while True:
        try:    
            inco = int(input('In what increments? '))
            break
        except ValueError:
            print('Enter a valid input')

    start = coFrom
    end = endCo
    increment = inco

    while start <= end:
        time.sleep(1)
        start += increment
        times += 1
        if start > end:
            start -= increment
            remainder = end - start
            times -= 1
            print("\n", str(increment), "only went in", str(endCo), str(times), "times", "with a remainder of", remainder)
            starCo = False
            break
        print(start)
#Exit
input('\nPress <enter> to exit')
    



