class TeamMember():
    def __init__(self, **kwargs):
        self.data = dict() 
        for info in kwargs:
            self.data[info] = kwargs[info]
    def print_info(self):
        print(f"{self.data['name']} {self.data['surname']}. Programs in the {self.data['language']} language.")
 
members = list()
amount = int(input('How many participants would you like to register? '))
for i in range(amount):
    data = input('Enter the first name, last name, age, and programming language in a single line separated by spaces: ').split()
    members.append(TeamMember(name = data[0], surname = data[1], age = int(data[2]), language = data[3]))
 
youngest = members[0]
for member in members:
    if member.data['age'] < youngest.data['age']:
        youngest = member
 
print('Data on the youngest participant at the hackathon:')
youngest.print_info()
