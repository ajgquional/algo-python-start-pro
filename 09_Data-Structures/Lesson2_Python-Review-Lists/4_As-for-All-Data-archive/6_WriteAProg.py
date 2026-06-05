subjects = list()
subject = input('Enter subject (0 - stop input): ')
subject = subject.lower()

while subject != '0':
    if subject in subjects:
        print('This subject has already been recorded')
    else:
        subjects.append(subject)
    subject = input('Enter subject (0 - stop input): ')
    subject = subject.lower()
    
subjects.sort()
print('List of subjects:', subjects)