voices = {'ProTeam':0, 'IT-Power':0, 'SuperTech':0,'YodaCode':0}
 
vote = input("What team would you like to vote for? ")
while vote != 'stop':
   if vote in voices.keys():
       voices[vote] += 1
   else:
       print('There is no such team')
   vote = input("What team would you like to vote for? ")
 
best_team_value = 0
best_team_key = '0'
for i in voices.keys():
   if voices[i] > best_team_value:
       best_team_key = i
       best_team_value = voices[i]
 
print("The winning team is", best_team_key)
print("Votes -", best_team_value)
