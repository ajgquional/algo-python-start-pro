from time import time

rest = 30
move = ''
beginning = time()
while rest > 0 and move != 'off':
    move = input('Your move (off - resign): ')
    end = time()
    rest = 30 - (end - beginning)/60
    print('Time left', int(rest), 'minutes of 30')
