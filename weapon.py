class Weapon:
    def __init__(self):
        self.name = ""
        self.attack_power = 0

    def set_name (self, name):
        self.name = name
        return self.attack_power
    
    def set_power (self,power):
        self.attack_power = power
        return self.attack_power