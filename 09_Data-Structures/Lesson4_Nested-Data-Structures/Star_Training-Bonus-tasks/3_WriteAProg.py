def remove_inefficient(staff):
    bad_staff = ''
    for bad_staff in staff:
        if staff[bad_staff]['performance'] < 50:
            print('Employee', bad_staff, 'recommended for dismissal')
            return bad_staff
 
staff = {
   'Brown': {
       'position': 'marketing',
       'performance': 71
   },
   'Davis': {
       'position': 'marketing',
       'performance': 65
   },
   'Garcia': {
       'position': 'marketing',
       'performance': 49
   },
   'Miller': {
       'position': 'marketing',
       'performance': 53
   }
}

bad_staff = remove_inefficient(staff)
if bad_staff in staff:
    del staff[bad_staff]
    
print('Effective employees:')
for s in staff:
    print(s)