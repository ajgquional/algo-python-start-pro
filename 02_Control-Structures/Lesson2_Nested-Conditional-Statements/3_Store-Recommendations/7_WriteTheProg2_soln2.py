price1 = int(input('Price of product 1: '))
price2 = int(input('Price of product 2: '))
price3 = int(input('Price of product 3: '))
# search for the highest price
if price1 <= price2:
   price1 = price2
if price1 <= price3:
   price1 = price3
print('Promotion! Total for three items:', price1)