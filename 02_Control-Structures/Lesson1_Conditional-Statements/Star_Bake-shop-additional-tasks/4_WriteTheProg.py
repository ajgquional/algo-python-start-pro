weight = int(input('Enter weight of the cake in grams: '))
taste = input('Enter filling: ')
if weight <= 2500:
   price = 3000
else:
   price = 5000
if taste == 'fruit':
   price = price + 1000
else:
   price =  price + 500
print('Approximate cake price:', price)