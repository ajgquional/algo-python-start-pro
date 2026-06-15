count = int(input('Number of users: '))
for i in range(count):
    login = input('Login: ')
    age = int(input('Age: '))
    if age >= 14:
        print('Account created:', login)
    else:
        print('Error: less than 14 years old.')
