name = input('Trainee name: ')
tasks_main = int(input('Number of mandatory tasks: '))
tasks_add = int(input('Number of extra tasks: '))
efficiency =  tasks_main*15 + tasks_add*20
print(name, '- performance', efficiency)