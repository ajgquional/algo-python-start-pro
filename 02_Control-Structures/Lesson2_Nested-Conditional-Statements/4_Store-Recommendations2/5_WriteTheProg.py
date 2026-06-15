total = int(input('Amount: '))
time = int(input('Current time (hour): '))
if time >= 20 and time <= 22:
  total = total/2
  print('Promotion! Total to pay:', total)
elif time >= 8 and time < 20:
  print('Total to pay:', total)
else:
  print('The store is closed!')