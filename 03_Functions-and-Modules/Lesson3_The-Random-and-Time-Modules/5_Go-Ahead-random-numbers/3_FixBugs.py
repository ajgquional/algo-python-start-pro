from random import randint

win_number = 1010
current_number = randint(1000, 3112)
print('Lottery ticket number is:', current_number)
if current_number == win_number:
    print('You won dinner at a restaurant!')
else:
    print('Better luck next time!')
