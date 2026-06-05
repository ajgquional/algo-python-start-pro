my_number = 9 #the secret number, do not change
number = int(input('I thought of a number from 1 to 10. Guess it: '))

while my_number != number:
    if my_number < number:
        number = int(input('No, my number is lower! Try again: '))
    else:
        number = int(input('No, my number is higher! Try again: '))

print('You guessed it!')