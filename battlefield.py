import random
from robot import Robot
from dinosaur import Dinosaur
import time
class Battlefield:
    def __init__(self):
        self.fleet.addFleet()
        self.herd.addHerd()
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
        select_number = random.randrange(1,2)
        if select_number == 1:
            return robot
        else:
            return dino

    def random_battle (self, robot, dino):
        self.victor = ""
        while True:
            select = Battlefield()
            attack_robot = Dinosaur()
            attack_dino = Robot()
            attacker = select.random_select(robot,dino)
            if attacker == robot:
                attack_robot.attack_from_robot(robot)
                print("Robot attack!")
            elif attacker == dino:
                attack_dino.attack_from_dino(dino)
                print("Dinosaur attack!")
                if dino.health < 0:
                    self.victor = robot
                    break
                elif robot.health < 0:
                    self.victor = dino
                    break
        return self.victor




    def display_winner(self):
        void
  