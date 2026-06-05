marks = input('Enter grades separated by spaces(The maximum grade is 5, the minimum grade is 0.): ')
marks = marks.split(' ')
print('Set analysis', marks)
growth = 1 # by default everyone has growth

for i in range(len(marks)-1):
    if marks[i+1] < marks[i]:
        growth = -1

if growth == 1:
    print('Stable performance!')
else:
    print('The performance is not stable')