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
        print('Greet the hero ->', self.name)
        print('Health level:', self.health)
        print('Armor class:', self.armor)
        print('Power of the strike:', self.power)
        print('Weapon:', self.weapon, '\n')

    #striking:
    def strike(self, enemy):
        print(
            '-> STRIKE! ' + self.name + ' attacks ' + enemy.name
            + ' with power ' + str(self.power) + ', using ' + self.weapon + '\n')
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print(
            enemy.name + ' swayed.\nArmor class dropped to ' +
            str(enemy.armor) + ', and health level dropped to ' + str(enemy.health) + '\n')


knight = Hero('Richard', 50, 25, 20, 'sword')
rascal = Hero('Helen', 20, 5, 5, 'bow and arrow')
knight.print_info()
rascal.print_info()
knight.strike(rascal)
