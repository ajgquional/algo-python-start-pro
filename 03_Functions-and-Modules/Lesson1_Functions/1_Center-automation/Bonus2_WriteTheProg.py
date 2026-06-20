def set_status(score):
    print('Your discount:')
    if score > 0 and score < 50:
        print('10% discount')
    elif score >= 50 and score < 100:
        print('15% discount')
    elif score >= 100:
        print('20% discount')


score = int(input('Points earned: '))
set_status(score)
