n = int(input('Enter the company’s budget: '))
x = int(input('Enter a senior developer’s salary: '))
y = int(input('Enter a middle developer’s salary: '))
z = int(input('Enter a junior developer’s salary: '))

qual1 = n//x
balance = n%x
qual2 = balance//y
balance = balance%y
qual3 = balance//z
balance =balance%z

print('Number of senior developers',qual1)
print('Number of middle developers',qual2)
print('Number of junior developers',qual3)
print('Remaining funds after distribution',balance)
