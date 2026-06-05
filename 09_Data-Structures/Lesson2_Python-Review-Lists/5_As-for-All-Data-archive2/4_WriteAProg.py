marks = input('Enter grades separated by spaces(minimum is 1, maximum is 5): ')
marks = marks.split(' ')
amount_five = 0

for mark in marks:
    if mark == '5':
        amount_five += 1

chance = amount_five/len(marks)*100
print('Perfection factor (%) -', chance)