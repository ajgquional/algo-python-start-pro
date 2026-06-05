readers = {214: 'Smith, secondary school', 122: 'Williams, high school', 59: 'Holmes, university', 368: 'Watson, secondary school'}
number = input('Welcome! Your library card number: ')

while True:
    try:
        number = int(number)
        break
    except:
        number = input('Enter the number in figures: ')

if number in readers:
    print('Hello, reader', readers[number])
else:
    print('This library card was not found!')