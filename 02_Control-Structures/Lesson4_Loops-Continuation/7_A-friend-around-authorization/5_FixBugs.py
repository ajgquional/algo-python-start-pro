total = 0
count = int(input('Number of marks: '))
for i in range(count):
    mark = int(input('Mark: ')) 
    total += mark
print('Average:', total/count)
