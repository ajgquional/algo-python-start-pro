def total_score(amount):
    score = 0
    for i in range(amount):
        mark = int(input('Enter the grade: '))
        score += mark
    print('Total score:', score)
    return score


def give_reward(subjects):
    score = total_score(subjects)
    if score > 80:
        print('Award with a diploma.')
    elif score > 50:
        print('Award with a certificate of commendation.')
    else:
        print('Issue a certificate of participation.')


name = input('Enter name: (stop - finish): ')
while name != 'stop':
    subjects = int(input('Number of subjects studied: '))
    give_reward(subjects)
    name = input('Enter name: (stop - finish): ')