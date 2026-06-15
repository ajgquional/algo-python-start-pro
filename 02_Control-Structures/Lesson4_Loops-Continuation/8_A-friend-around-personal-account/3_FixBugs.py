number = input('Enter 1 - recommendation, off - complete ')
while number != 'off':
    if number == '1':
        preference = input('Your mood: ')
        if preference == 'happy':
            print('Shrek')
        else: 
            print('Aladdin')
    number = input('Enter 1 - recommendation, off - exit ')
