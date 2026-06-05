trainings = {
    'Onboarding' : {
        'Person in charge' : 'James B.',
        'Topics' : ['accident prevention', 'teamwork'],
        'Date' : 15.05
    },
    'Professional development' : {
        'Person in charge' : 'Jessica S.',
        'Topics' : ['leadership', 'computer skills'],
        'Date' : 20.11
    },
}

print("ProTeam training sessions")
print("1-names of training sessions, 2-info on training session")

action_num = ''

while action_num != 'off':
    action_num = str(input("Action number (off-exit):"))
    if action_num == '1':
        for training in trainings:
            print('- ' + training)

    elif action_num == '2':
        training_name = str(input("Name of training session: "))
        if training_name in trainings:
            for vals in trainings[training_name].values():
                print(vals)

        else:
            print("That training session does not exist!")
