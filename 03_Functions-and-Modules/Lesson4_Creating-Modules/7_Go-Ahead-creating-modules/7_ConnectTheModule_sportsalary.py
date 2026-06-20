import sport_salary

surname = input('Coach surname: ')
job = input('Employment (1-full, 2-hourly): ')
if job == '1':
    experience = int(input('Experience in years:'))
    salary = sport_salary.get_full_time(experience)
elif job == '2':
    hours = int(input('Hours worked: '))
    salary = sport_salary.get_part_time(hours)
print(surname, '-', salary)
