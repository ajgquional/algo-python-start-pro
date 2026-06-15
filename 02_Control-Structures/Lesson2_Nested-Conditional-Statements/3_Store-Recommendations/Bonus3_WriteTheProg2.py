category = input('Category: ')
if category == 'products':
   price = int(input('Price: '))
   if price < 100:
       print('Try our baked goods!')
   if price >= 100 and price < 500:
       print('How about the chocolate-covered nuts?')
   if price >= 500:
       print('Try some exotic fruits!')
else:
   print('Look at the household goods!')