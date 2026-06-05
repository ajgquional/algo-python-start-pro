number = int(input('Enter the number: '))
i = 1
total = 0

while i <= number:
    total += i
    i += 1

print('The sum of the numbers from 1 to', number, 'is', total)