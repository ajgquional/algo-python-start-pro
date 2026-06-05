students = ['Davis - 5', 'Garcia - 4', 'Brown - 3', 'Williams - 4', 'Miller - 5']
amount_students = len(students)
average_mark = 0

for student in students:
    mark = int(student[len(student)-1]) # the grade is the last symbol of any list item.(The maximum grade is 5, the minimum grade is 0.)
    average_mark += mark

average_mark = average_mark / len(students)
print('Average score:', average_mark)