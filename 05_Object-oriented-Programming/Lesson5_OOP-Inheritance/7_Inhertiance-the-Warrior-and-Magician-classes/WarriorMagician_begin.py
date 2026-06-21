from time import sleep

class Hero():
    #class constructor
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health #number
        self.armor = armor #string
    #print character parameters
    def print_info(self):
        print('Health level:', self.health)
        print('Armor class:', self.armor, '\n')

#then program the derived classes of the Hero superclass