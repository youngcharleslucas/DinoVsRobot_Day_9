import random
import time
class Battlefield:
    def __init__(self):
        # self.fleet.addFleet()
        # self.herd.addHerd()
        self.victor = ""
    def run_game(self):
        void

    def display_welcome(self):
        void

    def battle(self):
        void
    
    def dino_turn(self, dinosaur):
        void

    def robo_turn(self, robot):
        void

    def show_dino_opponent_options(self): 
        void

    def show_robo_opponent_options(self):
        void

    def attack_from_robot (self, dino, robot):
        dino.health = dino.health - robot.weapon.attack_power
        return dino.health


    def random_select(self, robot, dino):
        select_number = random.randint(1,2)
        if select_number == 1:
            return robot
        else:
            return dino

    def random_battle (self, robot, dino):
        self.victor = ""
        battle = True
        while battle == True:
            self.random_select(robot,dino)
            if self.random_select(robot,dino) == robot:
                dino.attack_from_robot(dino, robot)
                print(f"Robot attack! {dino.name} health {dino.health}")
                time.sleep(2)
                if dino.health <= 0:
                    self.victor = robot
                    battle = False
                    break
            else:
                robot.robot.attack_from_dino(dino)
                print(f"Dinosaur attack! {robot.name} health {robot.health}")
                time.sleep(2)
                if robot.health <= 0:
                    self.victor = dino
                    battle = False
                    break
        return self.victor




    def display_winner(self):
        void
  