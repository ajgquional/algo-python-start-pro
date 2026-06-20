def is_camp(grade):
    if grade > 50:
        return True
    else:
        return False
    
amount = int(input('Number of students: '))
for i in range(amount):
    grade = int(input('Enter the grade: '))
    res = is_camp(grade)
    print('Admitted:', res)
    if res == False:
        print('Get reading! Here are some great picks: The Catcher in the Rye, The Great Gatsby, Gone with the Wind')
