def check_price(old_price, new_price):
    if int(old_price*1.1) > new_price:
        return False
    return True
 
price = int(input('Enter the initial price: '))
new = int(input('Enter your price: '))
while new !=0:
    if check_price(price, new):
        price = new
        print('New price set:', price)
    else:
        print('Your price is too low')
    new = int(input('Enter your price: '))
print('Sold for', price)
