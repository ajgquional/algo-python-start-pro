souvenirs = {
   't-shirts': ['I love Hemingway!', 'But man is not made for defeat', 'Courage is grace under pressure.'],
   'bracelets': ['I am a reader and i am a winner', 'If we win here we will win everywhere'],
   'bags': ['With Hemingway on it', 'With Fitzgerald on it', 'With a pen']
}

print('Store product range:')
for category in souvenirs:
   print(category)
   for product in souvenirs[category]:
         print('-', product)

answer = int(input('What would you like to buy? 1- t-shirts, 2- bracelets, 3- bags '))
if answer == 1:
   print('To pay: 15 dollars')
elif answer == 2:
   print('To pay: 30 dollars')
elif answer == 3:
   print('To pay: 6 dollars')
else:
   print('Invalid number')