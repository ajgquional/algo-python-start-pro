category = input('Enter a type of baked good: ')
taste = input('Enter a flavor: ')
category = category.lower()
taste = taste.lower()
is_top = category == 'cake' and taste == 'chocolate'
print('The most popular query has been set:', is_top)