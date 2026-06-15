price = int(input('Product cost (0 - no more purchases): '))
cost = price
while price != 0:
    price = int(input('Product cost (0 - no more purchases): '))
    cost += price           
print('Cost of all purchases: ' + str(cost))
