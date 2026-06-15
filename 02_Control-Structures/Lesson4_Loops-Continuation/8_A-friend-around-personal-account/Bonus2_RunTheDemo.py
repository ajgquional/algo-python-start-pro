vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
 
password = input('Enter your password: ')
password = password.lower()
result = ''
for symbol in password:
    if symbol in vowels:
        result += '0'
    elif symbol in consonants:
        result += '1'
print(result)
