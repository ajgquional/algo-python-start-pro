from random import randint

# entering student names separated by spaces
students = input('Enter the last names of the students separated by spaces: ')

# creating a list of student names
students = students.split(' ')
amount = len(students)

# generating random version numbers
numbers = list()
for student in students:
    # generating a version number and adding it to the numbers list
    number = randint(1, amount)
    numbers.append(number)

# amount - number of students
print('Distribution of test versions')
for i in range(amount):
    print(students[i], '-', numbers[i])