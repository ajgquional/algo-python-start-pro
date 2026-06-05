marks = list()
amount_five = 0
amount_four = 0
amount_three = 0
mark = int(input('Enter grade (0 - stop input)(The maximum grade is 5, the minimum grade is 0.): '))

while mark != 0:
    if mark == 5:
        amount_five += 1
    if mark == 4:
        amount_four += 1
    if mark == 3:
        amount_three += 1
    marks.append(mark)
    mark = int(input('Enter score (0 - stop input): '))

progress = (amount_five + amount_four + amount_three)/len(marks)*100
print('Grade list:', marks)
print('Performance:', progress)