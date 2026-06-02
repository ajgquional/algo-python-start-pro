#deduction of state income tax
salary = int(input('Full employee salary: '))
tax = 0.13
tax = salary*tax
salary = salary - tax
print('Deducted from the salary:', tax)
print('The employee will receive:', salary)