authors = {
   'Woolf' : 'English writer, considered one of the most important modernist 20th-century authors and also a pioneer in the use of stream of consciousness as a narrative device',
   'Austen' : 'English novelist known primarily for her six major novels, which interpret, critique and comment upon the British landed gentry at the end of the 18th century',
   'Dickinson' : 'The greatest and most original poet of all time. She took definition as her province and challenged the existing definitions of poetry and the work of poet'}
surname = input('Last name of the author: ')

if surname in authors:
    print('Biography:', authors[surname])

else:
    answer = input('Author not found. Add them? ')
    answer = answer.lower()
    if answer == 'yes':
        biography = input('Their biography: ')
        authors[surname] = biography
        print(authors)
    else:
        print('Response received')