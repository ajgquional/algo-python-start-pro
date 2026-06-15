tickets = 500
price = 10

while tickets > 0:
    amount = int(input('How many tickets would you like to buy?: '))
    if tickets - amount < 0:
        print('Amount not available.', tickets, 'left for sale.')
    else:
        tickets -= amount
        print(amount, 'tickets sold. Cost:', amount*price, 'USD.')
print('All tickets sold out!')
