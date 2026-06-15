# buyer forecasting
amount1 = int(input('Enter the number of buyers the day before yesterday: '))
amount2 = int(input('Enter the number of buyers yesterday: '))
if amount2 > amount1:
   amount3 = amount2 + (amount2 - amount1)
elif amount2 < amount1:
   amount3 = amount2 - (amount1 - amount2)
else:
   amount3 = amount2
print ('Today the store will be visited by:', amount3, 'people')