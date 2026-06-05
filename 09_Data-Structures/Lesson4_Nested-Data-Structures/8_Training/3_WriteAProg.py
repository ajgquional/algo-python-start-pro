departments = {
   'sales':{
       'employees': ['Smith', 'Johns'],
       'manager': 'Johns',
       'head': 'Smith'
   },
   'development':{
       'employees': ['Jackson', 'Swift', 'Robbinson'],
       'manager': 'Swift',
       'head': 'Robbinson'
   }
}

# complete the output
print("Heads of departments:")
for dept in departments:
    print('- ' + departments[dept]['head'])

print("Department project managers:")
for dept in departments:
    print('- ' + departments[dept]['manager'])
