class Weapon:
    def __init__(self):
        self.name = ""
        self.attack_power = 0

    def set_attribute (self):
        self.name = input("What is the name of your weapon? ")
        print ("The name of your weapon is ", self.name)
        self.attack_power = int(input("How powerful is your weapon? (0-20) "))
        print ("Your weapon is at a power of ", self.attack_power)