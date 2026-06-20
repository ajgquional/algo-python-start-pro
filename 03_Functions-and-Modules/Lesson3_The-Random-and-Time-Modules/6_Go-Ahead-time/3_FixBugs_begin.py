from time import

rest = 30
begining = time()
while rest > 0 and move == 'off':
    move = input('Your move (off - resign):')
    end = time()
    rest = 30 - (end - begining)
    print('Time left', int(rest), 'minutes of 30')