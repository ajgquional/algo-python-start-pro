price1 = int(input('Price of product 1: '))
price2 = int(input('Price of product 2: '))
price3 = int(input('Price of product 3: '))
# checking the order of prices in ascending order
total = price1 + price2 + price3
if price1 < price2 and price2 < price3:
  total = total/2
  print('Promotion!')
# checking the order of prices in descending order
if price1 > price2 and price2 > price3:
  total = total/3
  print('Promotion!')
print('To pay:', total)