countries = {'Venezuela':2720,'Argentina':48.8,'Turkey':16.59,'Brazil':8.06,'Russia':6.02,'Iceland':4.3,'Belgium':1.63,'Australia':1.1}
border = int(input('Enter the inflation level: '))
lower = []
same = []
higher = []
for i in countries:
   if (countries[i]-border) > 5:
       higher.append(i)
   elif (countries[i]-border) < - 5:
       lower.append(i)
   else:
       same.append(i)
 
higher.sort()
lower.sort()
same.sort()
 
print('Countries with inflation rates above', border, '% -', ', '.join(higher))
print('Countries with inflation rates below', border, '% -', ', '.join(lower))
print('Countries with inflation rates close to', border, '% -', ', '.join(same))
