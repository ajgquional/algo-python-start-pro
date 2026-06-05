my_shelf = dict()
author = input('Enter an author (q - end): ')

while author != 'q':
    books = list()
    book = input('Enter a book (s - stop): ')
    
    while book != 's':
        books.append(book)
        book = input('Enter a book (s - stop): ')
    
    my_shelf[author] = books
    author = input('Enter an author (q - end): ')

for author in my_shelf:
    print(author, '-', my_shelf[author])