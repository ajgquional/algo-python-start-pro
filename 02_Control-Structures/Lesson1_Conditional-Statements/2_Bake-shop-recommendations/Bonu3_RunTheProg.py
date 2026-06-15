product = input('Enter the type of dessert: ')
if product == 'cake':
    taste = input('Enter the flavor of the cake: ')
    if taste == 'chocolate':
        print('Try the Prague cake!')
    else:
        print('How about a honey cake?')
else:
    print('Call us to check availability')