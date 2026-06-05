my_shelf = dict()
author = input('Enter an author: ')
book = input('Enter a book (s - stop): ')
books = list()

while book != 's':
    books.append(book)
    book = input('Enter a book (s - stop): ')
    
my_shelf[author] = books
print(my_shelf)