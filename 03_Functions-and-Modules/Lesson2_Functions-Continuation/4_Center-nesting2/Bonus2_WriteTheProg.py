def info_lab():
    print('The laboratory is in room A203.')
    question()


def info_lec(): 
    print('The lecture hall is in room A112.')
    question()


def question():
    answer = input('What are you interested in? (stop - exit): ')
    if answer == 'laboratory':
        info_lab()
    elif answer == 'lectures':
        info_lec()
    elif answer == 'stop':
        print('Goodbye!')


question()
