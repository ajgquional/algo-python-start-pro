books = {
   'King': 'It',
   'London': 'White Fang',
   'Carroll': 'Alice in Wonderland',
   'Lindgren': 'Karlsson on the Roof'}

# add 2 titles
books['Defoe'] = 'The Adventures of Robinson Crusoe'
books['Dumas'] = 'The Count of Monte Cristo'

# remove 1 title
del books['King']

if 'Defoe' in books and 'Dumas' in books:
    print('The catalog has been updated!')
if ('King' in books) == False:
    print('Preferences have been updated')