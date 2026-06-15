n = int(input('Enter the height: '))
i = 0
while i < n:
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    i += 1
