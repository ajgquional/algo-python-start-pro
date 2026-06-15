category = input('Category (off - when you are done): ')
while category != 'off':
    cost = int(input('Amount: '))
    if category == 'dairy products':
        print('Discount 10%. To pay: ' + str(cost * 0.9))
    elif category == 'baked goods':
        print('Discount 30%. To pay: ' + str(cost * 0.7))
    else:
        print('To pay: ' + str(cost))
    category = input('Enter product category: ')
print('Checkout closed.')
