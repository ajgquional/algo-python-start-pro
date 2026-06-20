def get_course(wish):
    if wish.find('sports') != -1:
        course = 'volleyball'
    elif wish.find('science') != -1:
        course = 'astronomy'
    elif wish.find('comics') != -1:
        course = 'sketching'
    else:
        course = 'history of ancient Rome'
    return course


amount = int(input('Number of students: '))
for i in range(amount):
    wish = input('Enter your wish: ')
    course = get_course(wish)
    print('Recommended:', course)
    if course == 'astronomy':
        print('Warning! Classes are held at night!')
