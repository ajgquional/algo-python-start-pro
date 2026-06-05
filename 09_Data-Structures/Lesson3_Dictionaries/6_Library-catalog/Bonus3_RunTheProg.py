class Reader:
    def __init__(self, Surname, Grade, Books):
        self.Surname = Surname
        self.Grade = Grade
        self.Books = Books
    def print_data(self):
        print(self.Surname, '-', self.Grade, '-', self.Books)
 
print('Creating a reader account')
surname = input('Enter last name: ')
grade = input('Enter grade: ')
 
Student_Reader = Reader(surname, grade, [])
answer = input('Want to take out a book? (yes/no) ')
if answer == 'yes':
    book = input('Book title (off - complete): ')
    while book != 'off':
        Student_Reader.Books.append(book)
        book = input('Book title (off - complete): ')
Student_Reader.print_data()