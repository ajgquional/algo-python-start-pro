#function for calculating the number of points
#def total_score(amount)

#function for printing the appropriate award
#def give_reward(subjects)

#main part of the program: reading data and running functions
name = input('Enter name: (stop - finish)')
while name != 'stop':
    subjects = int(input('Number of subjects studied:'))
    give_reward(subjects)
    name = input('Enter name: (stop - finish)')