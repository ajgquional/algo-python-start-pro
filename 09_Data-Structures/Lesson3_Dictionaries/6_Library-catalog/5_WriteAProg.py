# Data from one of the readers. Do not change!
student_card = {'number': '324', 'last name': 'Jackson'}
print('Welcome!', student_card)
answer = int(input('Personal account: 1 - take out, 2 - return, 3 - exit '))

while answer != 3:
    if answer == 1:
        title = input('Enter a title: ')
        student_card['checkouts'] = title
        print('Reader card: ', student_card)
    if answer == 2:
        if 'checkouts' in student_card:
            del student_card['checkouts']
        print('Reader card: ', student_card)
    answer = int(input('Your action: 1 - take out, 2 - return, 3 - exit '))

print('See you soon:', student_card)