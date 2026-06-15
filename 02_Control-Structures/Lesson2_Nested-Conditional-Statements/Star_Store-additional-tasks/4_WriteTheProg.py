answer = int(input('Rate our store from 1 to 5: '))
if answer == 5:
   print('We are working for you!')
elif answer < 5 and answer >= 3:
   wish = input('Could you please clarify what you didn’t like? ')
   print('Thank you for your feedback!')
else:
   print('We will call you to find out more!')