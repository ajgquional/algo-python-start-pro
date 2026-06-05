questions = {
   'What are KPIs?': {
       'An indicator of success' : 'Correct',
       'Employee salary ranking' : 'Incorrect',
       'List of company directors' : 'Incorrect',
       'Vacation calendar' : 'Incorrect'
   }
}

print('To complete the onboarding process, take this test: ')
for question in questions:
    print(question)
    correct_answer = 0
    i = 1
    for answer in questions[question]:
        print(i, answer)
        if questions[question][answer] == 'Correct':
            correct_answer = 1
        i += 1
    reply = int(input('Answer number: '))
    if reply == correct_answer:
        print('Correct answer')
    else:
        print('Incorrect answer')