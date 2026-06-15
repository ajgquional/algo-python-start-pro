question = input('Ask a question (stop - end): ')
while question != 'stop':
    if question == 'What is your name?':
        print('My name is Christina.')
    elif question == 'Do you have any hobbies?':
        print('I like drawing.')
    elif question == '':
        print('Ask me something.')
    else:
        print('Unfortunately, I don’t understand you.')
    question = input('Ask a question (stop - end): ')  
