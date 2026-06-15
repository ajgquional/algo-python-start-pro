ingredient = input('the main ingredient (stop - exit): ')
while ingredient != 'stop':
    time = input('1 - 30 minutes, 2 - 1 hour: ')
    if ingredient == 'cottage cheese':
        if time == '1':
            print('Casserole')
        elif time == '2':
            print('Cheese pancakes')
    elif ingredient == 'chicken':
        if time == '1':
            print('Chicken breast in a cream sauce')
        elif time == '2':
            print('Noodles with chicken in a mushroom cream sauce')
    else:
        if time == '1':
            print('Broccoli salad')
        elif time == '2':
            print('Cream of mushroom soup')
    ingredient = input('the main ingredient (stop - exit): ')
