class Animal():
    def __init__(self, species, voice):
        self.species = species
        self.voice = voice  
        
    def make_voice(self):
        print(self.voice)


my_animal = Animal('dog', 'Woof!')
print('I am a robot-' + my_animal.species + '. I know the Voice command:')
my_animal.make_voice()
