def staff_max_efficiency(workers):
    maximum = 0
    for worker in workers:
        if workers[worker]['performance'] > maximum:
            maximum = workers[worker]['performance']
    return maximum
 
def staff_min_efficiency(workers):
    minimum = 150
    for worker in workers:
        if workers[worker]['performance'] < minimum:
            minimum = workers[worker]['performance']
    return minimum
 
workers = {
   'Cooper': {
       'position': 'sales manager',
       'performance': 86
   },
   'Stanley': {
       'position': 'sales manager',
       'performance': 69
   },
   'Johnson': {
       'position': 'sales manager',
       'performance': 78
   },
   'Simpson': {
       'position': 'sales manager',
       'performance': 91
   },
   'Richards': {
       'position': 'sales manager',
       'performance': 99
   }
}

print('Best result:', staff_max_efficiency(workers))
print('Worst result:', staff_min_efficiency(workers))