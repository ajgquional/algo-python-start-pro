buy_ticket(price):
    ans = input('Would you like to take out insurance for the duration of the flight?')
    if ans == 'yes':
       price += 500
    ans = input('Would you like to purchase meals on board?')
    if ans == 'yes':
       price += 700
    return
 
price = 2000
final_price = buy_ticket()
print('Ticket price including services:', final_price)