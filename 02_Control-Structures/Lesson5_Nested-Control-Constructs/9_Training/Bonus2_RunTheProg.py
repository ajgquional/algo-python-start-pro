import random

length = int(input('Enter the preferred password length: '))
password = ''
for i in range(length):
    password = password + str(random.randint(0,9))
print(password)