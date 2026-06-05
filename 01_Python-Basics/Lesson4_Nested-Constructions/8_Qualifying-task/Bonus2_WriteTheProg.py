weekly_hours = int(input('Number of working hours in a week: '))
hour_salary = int(input('Desired hourly rate: '))
month_salary = hour_salary * weekly_hours * 4
print('Allocate from the budget:', month_salary)