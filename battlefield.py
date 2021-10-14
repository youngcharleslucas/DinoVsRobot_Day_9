import random
from robot import Robot
from dinosaur import Dinosaur
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

    def random_select(self, robot, dino):
        select_number = random.randint(1,2)
        if select_number == 1:
            return robot
        else:
            return dino

    def attack_from_attacker (self, defense, offense):
        self.health = self.health - offense.attack_power
        return self.health

    def random_battle (self, robot, dino):
        self.victor = ""
        battle = True
        while battle == True:
            if self.random_select(robot,dino) == robot:
                dino.health = dino.health - robot.weapon.attack_power
                print(f"Robot attack! {dino.name} health {dino.health}")
                time.sleep(2)
                if dino.health <= 0:
                    self.victor = robot.name
                    battle = False
                    break
            else:
                robot.health = robot.health - dino.attack_power
                print(f"Dinosaur attack! {robot.name} health {robot.health}")
                time.sleep(2)
                if robot.health <= 0:
                    self.victor = dino.name
                    battle = False
                    break
        return self.victor




    def display_winner(self):
        void
  