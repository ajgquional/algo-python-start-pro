answer = int(input('How many continents are there on Earth? '))
while answer != 7:
   if answer < 7:
       print('Not enough! There are more')
   else:
       print('Too many! There are fewer')
   answer = int(input('Try again: '))
print('Right. Their names: Europe, Asia, North America, South America, Africa, Australia, Antarctica')