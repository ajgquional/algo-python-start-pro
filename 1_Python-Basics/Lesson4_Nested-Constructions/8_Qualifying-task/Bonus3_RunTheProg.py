weekly_hours = int(input('Number of work hours per week: '))
hour_salary = int(input('Desired salary per hour: '))
month_salary = hour_salary * weekly_hours * 4
max_salary = 900000
if month_salary > max_salary:
    print('Not approved. This salary is not included in the budget.')
else:
    print('Approved. Allocate from the budget:', month_salary)