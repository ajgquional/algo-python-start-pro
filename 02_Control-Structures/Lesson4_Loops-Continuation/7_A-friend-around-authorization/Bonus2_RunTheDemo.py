password = input('Enter your password: ')
password = password.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for symbol in password:
    print(alphabet.find(symbol) + 1)
