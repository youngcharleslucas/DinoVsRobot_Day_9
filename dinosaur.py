class Dinosaur:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.attack_power = 0
    
    def set_name (self):
        self.name = input("What is the dinosaur name?: ")
        print("The dinosaur name is ",self.name)

    def set_attack_power (self):
        self.attack_power = int(input(f"What is the attack power of {self.name}?"))
        print(f"The attack power of {self.name} is {self.attack_power}")

    def attack (self, robot):
        void

   