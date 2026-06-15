password = input('Enter your login: ')
wrong = '=?*^$#@_'
for symbol in password:
    if symbol in wrong:
        print('Prohibited character: ', symbol)
