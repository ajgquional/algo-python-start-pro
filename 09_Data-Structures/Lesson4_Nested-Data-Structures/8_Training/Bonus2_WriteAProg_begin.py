questions = {
    'What are KPIs?': {
        'An indicator of success' : 'Correct',
        'Employee salary ranking' : 'Incorrect',
        'List of company directors' : 'Incorrect',
        'Vacation calendar' : 'Incorrect'
    }
}

print('To complete the onboarding process, take this test:')
for question in questions:
    #...

    for answer in questions[question]:
        #...

    if reply == correct_answer:
        #...