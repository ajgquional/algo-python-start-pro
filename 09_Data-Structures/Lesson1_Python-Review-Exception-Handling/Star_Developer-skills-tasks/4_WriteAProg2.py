a = int(input('Enter the first integer: '))
b = int(input('Enter the second integer: '))
c = int(input('Enter the third integer: '))

if a <= b and a <= c:
   print('The first is the smallest.')
if b <= c and b <= a:
   print('The second is the smallest.')
if c <= a and c <= b:
   print('The third is the smallest.')