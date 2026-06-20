from random import randint

total_teams = int(input('Enter the number of teams: '))
name = input('Name of the player (0 - end): ')
while name != '0':
    team_num = randint(1, total_teams)
    print(name + ', number of your team is', team_num)
    name = input('Name of the player (0 -  end): ')
