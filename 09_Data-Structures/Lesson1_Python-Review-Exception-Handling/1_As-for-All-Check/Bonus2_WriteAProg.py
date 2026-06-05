from time import *
start = time()
answer = input('Enter the greatest even number ')
if answer.find('no') != -1:
   print("Correct, you didn't fall for the trick!")
else:
   print('Wrong, there is no greatest even number')
end = time()
print('You answered in', end - start, 'seconds')