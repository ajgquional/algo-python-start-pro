feedback1 = input('Write a detailed comment: ')
feedback2 = input('What you liked: ')
feedback3 = input('What you disliked: ')
length1 = len(feedback1)
length2 = len(feedback2)
length3 = len(feedback3)
sale = (length1 + length2 + length3)*0.1
print('Thanks! Your discount:', sale)