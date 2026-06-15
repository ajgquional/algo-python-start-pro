pro_team = {
   'Smith':{
       'experience': 6,
       'skills': 7,
       'specialization': 'mobile developer',
       'portfolio': ['Among us','Roblox']},
   'Avery': {
       'experience': 3,
       'skills': 6,
      'specialization': '3D designer',
      'portfolio': ['World of Tanks tanks']
      },
   'Grey': {
       'experience': 5,
       'skills': 9,
      'specialization': 'motion designer',
      'portfolio': ['NFS', 'Minecraft']
      },
   'Shepard': {
       'experience': 2,
       'skills': 5,
      'specialization': 'Python developer',
      'portfolio': ['Flask', 'Django']
      }
}

staff = []
for st in pro_team.values():
    a = st['experience']*1.5+st['skills']*3+len(st['portfolio']*5)
    staff.append(a)

i = 0
for key in pro_team.keys():
    print(key,'-',staff[i])
    i += 1
