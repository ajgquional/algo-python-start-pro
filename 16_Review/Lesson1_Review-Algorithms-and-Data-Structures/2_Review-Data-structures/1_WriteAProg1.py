months = 'January February March April May June July August September October November December'.split()
sales = input('Enter the income data for January through December: ').split()
sales = list(map(int, sales))
growth = []
fall = []
for i in range(1, len(sales)):
    if sales[i] > sales[i-1]:
        growth.append(months[i])
    if sales[i] < sales[i-1]:
        fall.append(months[i])
print('Months of revenue growth:', growth) 
print('Months of declining income:', fall)
