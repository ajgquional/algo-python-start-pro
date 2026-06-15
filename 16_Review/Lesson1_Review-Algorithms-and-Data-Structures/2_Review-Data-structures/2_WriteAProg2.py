data = dict()
while input('Would you like to enroll in a programming lesson (yes/no)?: ').lower() == 'yes':
    topic = input('Enter the topic of the lesson: ')
    if topic in data:
        data[topic] += 1
    else:
        data[topic] = 1

total_lessons = 0
for lesson in list(data.values()):
    total_lessons += lesson
total_topics = len(data)

print('Total number of lessons:', total_lessons)
print('Topics considered:', total_topics)
