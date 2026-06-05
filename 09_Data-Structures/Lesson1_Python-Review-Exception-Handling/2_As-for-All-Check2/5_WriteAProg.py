print('What does WHO stand for?')
print('1-World Health Organization')
print('2-World Habitat Organization')
print('3-Worldwide Horticulture Organization')
print('4-Worldwide Happiness Organization')

while True:
    try:
        answer = int(input())
        break
    except:
        print('Error! Enter the number of the correct answer')

if answer == 1:
    print("That's right!")
else:
   print('No. WHO is the World Health Organization')