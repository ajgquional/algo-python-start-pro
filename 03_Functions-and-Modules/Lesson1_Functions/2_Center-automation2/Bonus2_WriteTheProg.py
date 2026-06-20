def is_ok(score):
    if score < 100:
        return False
    else:
        return True
   
score = int(input('Enter the score: '))
print('Merch available:', is_ok(score))
