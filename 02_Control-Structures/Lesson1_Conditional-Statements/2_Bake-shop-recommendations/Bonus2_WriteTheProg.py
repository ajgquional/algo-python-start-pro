weight = int(input('Enter weight of the dessert you want in kilograms: '))
if weight < 2:
   print('Try the tartlets with cream.')
if weight >= 2 and weight <= 3:
   print('How about assorted mini cakes?')
if weight > 3:
   print('We recommend a multi-tiered cake.')
print('Go shopping!')