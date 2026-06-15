category = input('Category in the "Straight from the garden" section: ')
if category == 'greens':
    max_price = int(input('Maximum price: '))
    if max_price >= 100:
        print('Try a salad mix')
    else:
        print('Try the assorted onions and parsley')
else:
    print('How about a sweet potato?')