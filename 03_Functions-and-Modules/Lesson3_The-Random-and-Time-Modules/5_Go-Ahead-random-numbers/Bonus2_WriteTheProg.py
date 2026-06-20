from random import randint

alphabet = 'ABCDEFGH'
line = alphabet[randint(0, 7)]
row = randint(1, 8)
move = line + str(row)
print('Move the piece on square', move)
