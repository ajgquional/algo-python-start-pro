# Task 2

def competition_result(team1, team2):
    score_1 = 0
    score_2 = 0
    goal_scoring = input('Who scored? (stop-exit) ')
    while goal_scoring != 'stop':
        if goal_scoring == team1:
            score_1 += 1
        elif goal_scoring == team2:
            score_2 += 1
        else:
            print('There is no such team!')
        goal_scoring = input('Who scored? (stop-exit) ')
    if score_1 > score_2:
        result = str(score_1) + ':' + str(score_2) + ', ' + team1 + ' won!'
    elif score_2 > score_1:
        result = str(score_1) + ':' + str(score_2) + ', ' + team2 + ' won!'
    else:
        result = str(score_1) + ':' + str(score_2) + ', tie!'
    return result
