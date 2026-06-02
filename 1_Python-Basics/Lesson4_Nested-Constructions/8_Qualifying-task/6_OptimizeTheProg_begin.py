month_salary = input('Enter the monthly salary:')
month_salary = int(month_salary)
vacation = input('Enter the number of vacation days:')
vacation = int(vacation)
month = 29.3 #average number of days in a month
daily_savary = month_salary/month
vacation_pay = daily_savary*vacation
print('Approximate vacation pay:', vacation_pay)