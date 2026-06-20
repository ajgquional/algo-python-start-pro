check_test(score):
    if score >= 80:
        return True
        else:
            return False
amount = int(input('Enter the number of participants:'))
for i in range(amount):
    name = input('Enter name:')
    score = int(input('Enter test score:'))
    res = check_test()
    print('Admitted:', res)