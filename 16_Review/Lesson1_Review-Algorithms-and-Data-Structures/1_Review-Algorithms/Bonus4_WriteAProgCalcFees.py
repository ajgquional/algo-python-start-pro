amount = input('Enter the amount to transfer: ')
for symbol in amount:
    if not(symbol in '1234567890'):
        separator = symbol
        break
commission = round(int(amount.replace(separator, '')) * 0.0095, 2)
print('Transfer fee:', commission, 'USD.')
