from time import *

start = time()
print('Enter the number of the false fact about the human body')
print('1-It is impossible to laugh at the same time as being tickled')
print('2-Human hair lives 2 to 5 years')
print('3-To take 1 step, you need to use 200 muscles')
print('4-A distant human ancestor had 6 fingers')

while True:
   try:
       answer = int(input())
       break
   except:
       print('Error! Enter a number without other characters')

if answer == 4:
   print("That's right!")
else:
   print('No, people have never had 6 fingers')

end = time()
print('Program runtime', end - start)