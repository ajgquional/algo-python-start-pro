def get_result(score):
    if score >= 85:
        return '1st place'
    elif score >=65 and score < 85:
        return '2nd place'
    elif score >=50 and score < 65:
        return '3rd place'
    else:
        return 'Better luck next time!'


def give_reward(result):
    if result == '1st place':
        return 'Trip to Dublin'
    elif result == '2nd place':
        return 'Bookstore gift certificate'
    elif result == '3rd place':
        return 'Board game'
    else:
        return 'Certificate of participation'
   

score = int(input('Enter the grade: '))
result = get_result(score)
reward = give_reward(result)
print('Your result:', result, '-', reward)
