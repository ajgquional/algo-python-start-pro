readers = {
   'smith15': ['Phantom', 'Book of math problems']
}

login = input('Enter login ')
if login in readers:
   print('Login successful! Your books')
   print(readers['smith15'])
else:
   answer = input('Login not found. Add it? (yes/no) ')
   if answer == 'yes':
         books = list()
         book = input('Login added. Enter the book you’d like (s - stop) ')
         while book != 's':
            books.append(book)
            book = input('Enter the book you’d like (s - stop) ')
         readers[login] = books

         print('Our readers:')
         for reader in readers:
            print(reader, '-', readers[reader])