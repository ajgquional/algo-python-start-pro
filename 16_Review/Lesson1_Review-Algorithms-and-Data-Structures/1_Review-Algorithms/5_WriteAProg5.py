balance = int(input('Enter the current balance: '))
while balance > 0 and input('Would you like to make a purchase (yes/no)?: ') == 'yes':
    price = int(input('Enter the price: '))
    if balance - price < 0:
        print('Insufficient funds!')
    else:
        balance -= price
        print('The sum of $', price, 'has been charged.')
print('Available funds: $', balance)
