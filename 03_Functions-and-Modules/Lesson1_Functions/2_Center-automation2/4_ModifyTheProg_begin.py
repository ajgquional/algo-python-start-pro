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
