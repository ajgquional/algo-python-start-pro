answer = input('Who wrote The Adventures of Tom Sawyer? ')
answer = answer.lower()
attempts = 1
while answer != 'mark twain':
   answer = input('Who wrote The Adventures of Tom Sawyer? ')
   answer = answer.lower()
   attempts += 1
print('Answer counted after', attempts, 'attempt(s)')