
from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.weapon = Weapon()

    def attack_from_dino (self, dinosaur):
        self.health = self.health - dinosaur.attack_power
        return self.health 

    def set_name(self,name):
        self.name = name
        return self.name
        

    def set_weapon_power(self, power):
        self.weapon.set_power(power)
        return self.weapon.name

    def set_weapon_name(self, name):
        self.weapon.set_name(name)
        return self.weapon.attack_power

    def set_health(self):
        return self.health

    def robot_character(self, name, weapon_name, power):
        self.set_name(name)
        self.weapon.set_name(weapon_name)
        self.weapon.set_power(power)