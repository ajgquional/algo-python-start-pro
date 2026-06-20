# Task 8

def get_ticket_price():
    price = 2000
    number = int(input('Order number:'))
    if number % 1000 == 0:
        price *= 0.8
    return price


def get_total_price():
    total = 0
    while input('Buy a ticket? (off - exit)') != 'off':
        current_price = get_ticket_price()
        print('Ticket price:', current_price)
        total += current_price
    print('Amount due:', total)
