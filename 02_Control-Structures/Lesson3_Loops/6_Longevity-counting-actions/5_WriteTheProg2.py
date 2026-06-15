attempts = 0
promo = ''
while attempts < 3 and promo != 'fresh':
   promo = input('Enter your promo code: ')
   attempts += 1
if promo == 'fresh':
   print('Accepted on attempt #',attempts)
