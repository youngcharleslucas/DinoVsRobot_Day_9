from robot import Robot
class Dinosaur:
    def __init__(self):
        self.name = ""
        self.health = 0
        self.attack_power = 0
    
    def set_name (self, name):
        self.name = name
        return self.name

    def set_attack_power (self, attack_power):
        self.attack_power = attack_power
        return self.attack_power

    def set_health (self, health):
        self.health = health
        return self.health

    def attack_from_robot (self, robot):
        self.health = self.health - robot.weapon.attack_power
        return self.health

    def dino_character (self, name, power, health):
        self.set_name(name)
        self.set_attack_power(power)
        self.set_health(health)
    