#coin shop
coins = 100
print('Your coins:', coins)
choice = input('1 - shop, 2 - watch an ad (+5), 3 - exit ')
while choice != '3':
    if choice == '1':
        choice_market = input('1 - sticker (50), 2 - t-shirt (100) ')
        if choice_market == '1':
            coins -= 50
        elif choice_market == '2':
            coins -= 100
    elif choice == '2':
        coins += 5
    print('Your coins:', coins)
    choice = input('1 - shop, 2 - watch an ad (+5), 3 - exit ')
