while True:
   try:
       children_amount = int(input('Enter the number of children: '))
       sweets_amount = int(input('Enter the number of candies: '))
       break
   except:
       print('Error! The number must be an integer')

try:
   portion = sweets_amount/children_amount
   print('Each child will receive', portion, 'candies')
except:
   print('Division error! Did 0 children come?')