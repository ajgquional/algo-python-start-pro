class Accounting():
    def __init__(self, account):
        self.account = account
    def pay_bill(self, amount):
        if self.account - amount >= 0:
            self.account -= amount
            print(f'{amount} rubles debited. Account balance: {self.account} rubles.')
        else:
            print('Insufficient funds to complete the operation.')
    def get_money(self, amount):
        self.account += amount
        print(f'{amount} rubles credited. Account balance: {self.account} rubles.')
 
amount = int(input('Enter the data about the account balance: '))
office = Accounting(amount)
while input('Would you like to perform an operation? (1 - yes, 2 - no): ') == '1':
    code = input('Enter the operation code (1 - deposit, 2 - charge): ')
    amount = int(input('Enter the sum: '))
    if code == '1':
        office.get_money(amount)
    else:
        office.pay_bill(amount)
print('Thanks for your work! Have a nice evening!')
