get_result(score):
    if score >= 85:
        return '1st place'
    elif score >= 65 and score < 85:
        return '2nd place'
    elif score >= 50 and score < 65:
        return '3rd place'
    else:
        return 'Better luck next time!'
score = input('Enter score:')
print('Your result:', get_result( ))