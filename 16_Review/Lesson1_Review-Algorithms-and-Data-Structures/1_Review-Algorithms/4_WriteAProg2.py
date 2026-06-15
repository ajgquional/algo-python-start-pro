if input('Do you have an idea for your own product (yes/no)?: ').lower() == 'yes':
    if input('Are you interested in getting investments (yes/no)?: ').lower() == 'no':
        print('We recommend you enroll in a business school.')
    else:
        print('You have every chance to get into a business accelerator!')
else:
    print('Thank you for participating in the survey!')
