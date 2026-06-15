tel = input('Enter phone number: ')
permitted = '0123456789+'
 
for symbol in tel:
    if symbol not in permitted:
        print('Invalid phone number!')
        break
