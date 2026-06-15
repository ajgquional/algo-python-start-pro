amount = input('Enter a number: ')
result = amount[len(amount)-3:]
amount = amount[:len(amount)-3]
while amount != '':
    if len(amount) >= 3:
        end = amount[len(amount)-3:]
        amount = amount[:len(amount)-3]
    else:
        end = amount
        amount = ''
    result = end + ' ' + result
print(result)
