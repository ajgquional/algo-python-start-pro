sales = input('Would you like promotional items? ')
if sales == 'yes':
    category = input('Enter a category: ')
    if category == 'sweets':
        print('Gummy fruit for 200 coins')
    else:
        print('Lingonberry juice for 140 coins')
else:
    print('Let us know if you change your mind!')