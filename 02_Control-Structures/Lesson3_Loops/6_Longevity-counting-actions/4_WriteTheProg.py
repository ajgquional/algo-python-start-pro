#Counting categories of goods
category = input('Category (end - when you are done): ')
count = 0
while category != 'end':
    count += 1
    category = input('Category (end - when you are done): ')
print('Total product categories: ' + str(count))
