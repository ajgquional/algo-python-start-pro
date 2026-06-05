a = int(input('First side: '))
b = int(input('Second side: '))
c = int(input('Third side: '))

if a == b and a == c:
   print('Equilateral triangle.')
elif (a == b and a != c) or (b == c and a != c) or (a == c and a != b):
   print('Isosceles triangle.')
else:
   print('All the sides are different lengths.')