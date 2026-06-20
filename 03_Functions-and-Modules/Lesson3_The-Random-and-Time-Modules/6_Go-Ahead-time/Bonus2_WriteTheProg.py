from time import *

answer = input('Send off the field? (yes/no): ')
if answer == 'yes':
    period = int(input('For how many minutes? (2/10): '))
    print('You are sent off the field for', period, 'minute(-s)')
    sleep(period*60)
    print('Get back to the field!')
