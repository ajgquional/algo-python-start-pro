def check(q):
    if 10000 > q > 8000:
        print('Optimal amount.')
    elif q >= 10000:
        print('Approval required!')
    elif q <= 8000:
        print('Amount below average.')

        
money = int(input('Amount needed (0 - stop): '))
all_money = 0
while money != 0:
    all_money += money
    check(money)
    money = int(input('Amount needed (0 - stop): '))
print('Total money requested:', all_money)
