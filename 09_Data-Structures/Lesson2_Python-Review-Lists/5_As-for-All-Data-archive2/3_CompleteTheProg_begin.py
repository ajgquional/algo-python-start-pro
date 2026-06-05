#add grade input separated by spaces, the maximum grade is 5, the minimum grade is 0.

print('Set analysis', marks)
growth = 1 #by default everyone has growth
for i in range(len(marks)-1):
    if marks[i+1] < marks[i]: #if the current grade is lower than the next
        growth = -1 #performance is not stable

#add the output of results