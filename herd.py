from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.t_rex = Dinosaur()
        self.utahraptor = Dinosaur()
        self.ankylosaurus = Dinosaur()



    def dino_trex(self):
        self.t_rex.set_name("T-rex")
        self.t_rex.set_attack_power(19)
        self.t_rex.set_health(100)

    def attack_from_robot (self, dino, robot):
        dino.health = dino.health - robot.weapon.attack_power
        return dino.health


    #     self.t_rex.dino_character("T-rex", 19, 100,)
    #     self.utahraptor.dino_character("Utahraptor", 16, 100)
    #     self.ankylosaurus.dino_character("Ankylosaurus", 13, 120)

    # def trex_dino(self):
    #     self.trex