message = 'HHeelloo!!  HHooww aarree  yyoouu??  TThhee  wweeaatthheerr  iiss  ssoo  nniiccee  ttooddaayy..  SShhaallll  wwee  ttaakkee  aa  wwaallkk??'
 
result = ''
for i in range(0, len(message), 2):
    result += message[i]
 
print(result)
