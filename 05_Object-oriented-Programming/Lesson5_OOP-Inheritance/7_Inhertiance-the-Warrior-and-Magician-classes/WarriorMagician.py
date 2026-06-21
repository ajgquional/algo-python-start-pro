from time import sleep
 
class Hero():
    # class constructor
    def __init__(self, name, health, armor):
        self.name = name # string
        self.health = health # number
        self.armor = armor # number

    # print character parameters:
    def print_info(self):
        print('Health level:', self.health)
        print('Armor class:', self.armor, '\n')
 
'''Whatever is higher is given in the level initially'''
 
class Warrior(Hero):
    def hello(self):
        print('-> NEW HERO. A brave warrior appears riding a horse who is named', self.name)
        self.print_info()
        sleep(4)

    def attack(self, enemy):
        print('-> HIT! A brave warrior', self.name, 'is attacking', enemy.name, 'by sword!')
        enemy.armor -= 15 # strike force for the Warrior class
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print("A terrible blow fell upon the enemy. \n Now it's armor: " + str(enemy.armor) + ', and health level: ' + str(enemy.health) + '\n')
        sleep(5)
 
class Magician(Hero):
    def hello(self):
        print('-> NEW HERO. Out of nowhere, a skilled wizard appears', self.name)
        self.print_info()
        sleep(4)
 
    def attack(self, enemy):
        print('-> HIT! The agile magician', self.name, 'casts a spell on', enemy.name)
        enemy.armor -= 35 # strike force for the Magician class
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print('The complicated spell stuns the enemy. \n Now his armor: ' + str(enemy.armor) + ', and health level: ' + str(enemy.health) + '\n')
        sleep(5)
 
 
warrior1 = Warrior('Henry', 100, 50)
warrior1.hello()
 
magician1 = Magician('Luke', 50, 20)
magician1.hello()
 
warrior1.attack(magician1)
magician1.attack(warrior1)
