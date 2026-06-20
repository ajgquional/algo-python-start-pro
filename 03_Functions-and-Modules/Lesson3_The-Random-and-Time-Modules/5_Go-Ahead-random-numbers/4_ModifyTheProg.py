from random import randint

race1_participants = 0
race2_participants = 0

while input('Give the race number (off - stop)? ') != 'off':
    race_number = randint(1, 2)
    print('Your number is', race_number)
    if race_number == 1:
        race1_participants += 1
    else:
        race2_participants += 1
    print('Race 1 participants are', race1_participants)
    print('Race 2 participants are', race2_participants)
