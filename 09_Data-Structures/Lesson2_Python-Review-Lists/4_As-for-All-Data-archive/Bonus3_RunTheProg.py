marks = input('Enter grades separated by spaces: ')
marks = marks.split(' ')
honours_student = 0
for mark in marks:
    if mark == '5':
        honours_student += 1
print('Grades received:', marks)
print('Number of honor students:', honours_student)