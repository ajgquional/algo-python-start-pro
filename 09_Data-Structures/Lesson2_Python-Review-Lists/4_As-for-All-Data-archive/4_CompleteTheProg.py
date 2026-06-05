students = ['Addington', 'Benson', 'Clifford', 'Dalton', 'Emsworth', 'Graham']
amount_students = len(students)
students.sort()
i = 1
print('Class list:')
for student in students:
    print(i, '-', student)
    i += 1
print('Total students:', amount_students)