start_year = int(input('Year of registration: '))
end_year = int(input('Year of de-registration: '))
data = dict()
for year in range(start_year, end_year+1):
    data[year] = dict()
for year in range(start_year, end_year+1):
    while input('Would you like to add the topic for the projects of year ' + str(year) + ' (yes/no)?: ') == 'yes':
        topic = input('Enter the topic: ')
        projects = list(map(int, input('Enter the data about the numbers of applications (in a single line, separated by spaces): ').split()))
        if topic in data[year]:
            data[year][topic] += projects
        else:
            data[year][topic] = projects

projects = dict()
for year in data:
    for topic in data[year]:
        total = 0
        for amount in data[year][topic]:
            total += amount
        if topic in projects:
            projects[topic] += total
        else:
            projects[topic] = total

print('ANALYSIS RESULTS:')
total = 0
for topic in projects:
    print(topic, '-', projects[topic], 'projects.')
    total += projects[topic]
print('Total number of projects:', total)
