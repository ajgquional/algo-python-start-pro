answer = input('Do you want to explore our top sellers? ')
if answer == 'yes':
   category = input('Category of interest: ')
   if category == 'food':
       print('Milk 1l, Raisin cookies, Peaches')
   else:
       print('Laundry detergent, Shoe brush')
else:
   print('Let us know if you change your mind!')