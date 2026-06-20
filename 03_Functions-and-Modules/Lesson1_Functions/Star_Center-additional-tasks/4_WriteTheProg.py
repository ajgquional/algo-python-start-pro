def print_paper(st_name, st_class):
    print(
        'We would like to express our gratitude towards', st_name, 'from', st_class, 

        'class. The teaching staff of SUCCESS congratulates you on the end of this school year and wishes you future accomplishments in your studies.')
 

n = int(input('Number of straight A students: '))
for i in range(n):
    st_name = input('Enter name: ')
    st_class = input('Enter grade: ')
    print_paper(st_name, st_class)
