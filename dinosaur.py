class Dinosaur:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.attack_power = 0
    
    def set_name (self, name):
        self.name = name
        return self.name

    def set_attack_power (self, power):
        self.attack_power = int(input(f"What is the attack power of {self.name}?"))
        print(f"The attack power of {self.name} is {self.attack_power}")

    def attack_from_robot (self, robot):
        self.health = self.health - robot.weapon.attack_power
        return self.health
    def set_health (self):
        return self.health
   