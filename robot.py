
from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = 0
        self.health = 100
        self.weapon = Weapon()

    def attack_from_dino (self, dinosaur):
        self.health = self.health - dinosaur.attack_power
        return self.health 

    def set_name(self):
        self.name = input("Robot name: ")
        print ("Robot name is ", self.name)

    def set_weapon(self):
        self.weapon.set_attribute()
        return self.weapon.attack_power

    def set_health(self):
        return self.health