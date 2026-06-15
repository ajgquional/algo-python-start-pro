answer = input('Would you like to see our unusual assortment? ')
if answer == 'yes':
   product = input('Enter product type: ')
   if product == 'drink':
       taste = input ('Enter flavor: ')
       if taste == 'lemon':
           print('Try the Lime Cactus lemonade!')
       elif taste == 'apple':
           print('Try the baked apple soda')
       else:
           print('Try the Naughty Blackberry drink')
   else:
       print('Try the juniper pie!')
else:
   print("Oh well! We'll be waiting for you")