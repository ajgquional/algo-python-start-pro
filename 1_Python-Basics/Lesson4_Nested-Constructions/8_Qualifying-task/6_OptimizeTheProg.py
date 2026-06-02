month_salary = int(input('Enter a monthly salary: '))
vacation = int(input('Enter the number of vacation days: '))
daily_savary = month_salary/29.3 #average number of days in a month
vacation_pay = daily_savary*vacation
print('Approximate vacation pay:', vacation_pay)