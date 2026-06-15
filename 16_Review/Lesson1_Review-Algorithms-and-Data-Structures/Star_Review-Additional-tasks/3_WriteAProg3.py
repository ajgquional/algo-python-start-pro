max_count = 0
count = 1
income = list(map(int,input('Amount of income by month (separated by spaces): ').split()))
for i in range(1,len(income)):
   if income[i]>= income[i-1]:
       count +=1
   else:
       count = 1
   if count > max_count:
       max_count = count
if len(income) ==1:
   print(1)
else:
   print(max_count)
