code = input('0 - get a ticket, 1 - turn off the device: ')
number = 1
while code != '1':
    if code == '0':
        print('ticket number ' + str(number))
        number += 1
    code = input('0 - get a ticket, 1 - turn off the device: ')
