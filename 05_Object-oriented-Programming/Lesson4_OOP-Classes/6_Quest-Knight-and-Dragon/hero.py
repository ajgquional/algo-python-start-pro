from random import randint
from time import sleep
 
class Hero():
    # class constructor
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health # number
        self.armor = armor # string
        self.power = power # number
        self.weapon = weapon # string

    # print character info:
    def print_info(self):
        print('->' + self.name)
        print('Health level:', self.health)
        print('Armor class:', self.armor)
        print('Power of the strike:', self.power)
        print('Weapon:', self.weapon, '\n')
    
    # striking another character
    def strike(self, enemy):
        attack = randint(self.power-5, self.power+5)
        print('-> STRIKE! ' + self.name + ' attacks ' + enemy.name + ' with power ' + str(attack) + ', using ' + self.weapon + '\n')

        enemy.armor -= attack
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        
        print(enemy.name + ' swayed.\n Armor class dropped to ' + str(enemy.armor) + ', and health level dropped to ' + str(enemy.health) + '\n')

    # starting a fight
    def fight(self, enemy):
        while self.health and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, 'has fallen in this difficult battle!\n')
                break
            sleep(5)

            enemy.strike(self)
            if self.health <= 0:
                print(self.name, 'has fallen in this difficult battle!\n')
                break
            sleep(5)
