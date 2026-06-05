trips = ['the london eye', 'zsl london zoo', 'westminster abbey', 'madame tussauds museum']
searching = input('Request: ')
searching = searching.lower()
if searching in trips:
    print('Request found')
else:
    print('No such request')