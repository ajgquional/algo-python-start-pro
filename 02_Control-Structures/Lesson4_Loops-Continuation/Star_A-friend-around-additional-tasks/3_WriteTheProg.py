hero = input('Enter a character (off-exit): ')
while hero != 'off':
    if hero == 'Peter Parker':
        print('Spider-Man')
    elif hero == 'Aslan':
        print('The Chronicles of Narnia')
    elif hero == 'Jack Sparrow':
        print('Pirates of the Caribbean')
    elif hero == 'Master Shifu':
        print('Kung Fu Panda')
    elif hero == 'Fiona':
        print('Shrek')
    else:
        print("I don't know that character yet:(")
    hero = input('Enter a character (off-exit): ')
