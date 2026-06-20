import sport_rules

print('Today\'s program:\n1 - football\n2 - hockey\n3 - 100 meters race')
answer = input('Your choice (off - exit): ')
while answer != 'off':
    if answer == '1':
        sport_rules.print_football()
    elif answer == '2':
        sport_rules.print_hockey()
    elif answer == '3':
        sport_rules.print_sprint()
    else:
        print('Sport not found!')
    answer = input('Your choice (off - exit): ')
