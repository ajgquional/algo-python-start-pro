from random import randint

group1 = int(input('The number of members in team 1: '))
group2 = int(input('The number of members in team 2: '))
swimmer1 = randint(1, group1)
swimmer2 = randint(1, group2)
print('Swimmer', swimmer1, '- Swimmer', swimmer2)
