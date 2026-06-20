def buy_ticket(price):
    ans = input('Would you like to take out insurance for the duration of the flight? ')
    if ans == 'yes':
        price += 20
    ans = input('Would you like to purchase meals on board? ')
    if ans == 'yes':
        price += 50


    return price


price = 100
final_price = buy_ticket(price)
print('Ticket price including services:', final_price)
