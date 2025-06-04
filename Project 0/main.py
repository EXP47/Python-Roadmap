import random

rand_int = random.randint(1,100)
state = True

while state:
    numInput = int(input("Enter a number: "))
    if rand_int == numInput:
        state = False
        print('You guessed correctly')
        break
    elif rand_int > numInput:
        print('Your guess is too low')
    elif rand_int < numInput:
        print('Your guess is too high')
