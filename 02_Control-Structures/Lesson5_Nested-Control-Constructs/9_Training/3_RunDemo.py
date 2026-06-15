true_month = '7'
true_year = '2007'
 
for i in range(5):
    month = input('Month: ')
    year = input('Year: ')
    if month == true_month: 
        if year == true_year:
            print('You win!')
            break
        else:
            print('You guessed the month!')
    else:
        if year == true_year:
            print('You guessed the year!')
        else:
            print('Incorrect month and year.')
