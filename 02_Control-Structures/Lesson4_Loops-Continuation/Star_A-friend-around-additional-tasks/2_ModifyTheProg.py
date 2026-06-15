for i in range(3):
    login = input('Login: ')
    password = input('Password: ')
    if login == 'admin' and password == 'trGd3j':
        print('Authorization completed on attempt', i+1)
        break
if login != 'admin' or password != 'trGd3j':
    print('Access denied')
