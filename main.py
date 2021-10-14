'''
Robots vs. Dinosaurs User Stories
Out of 80 points
Using the concepts of OOP by creating classes and using objects (instances of those classes) to interact with each other, create a console application 
that will have robots and dinosaurs fight in a battle.
Before you begin the last user story that is highlighted in grey, write an algorithm that represents the steps of the robots in the fleet 
and the dinosaurs in the herd battling. Think about the steps that need to happen to implement the functionality. Please submit to your 
instructor Slack channel once completed for approval to start coding.

User stories:

A. (/5 points): As a developer, I want to make at least 7 commits with good, descriptive messages.

-B. (/5 points): As a developer, I want to make a class for each of the following: Robot, Dinosaur, Fleet, Herd, Weapon, Battlefield.

-C. (/10 points): As a developer, I want a Robot to have a name, health, and a Weapon (this needs to be its own class and object) with a 
   name (i.e. sword) and attack power.

-D. (/10 points): As a developer, I want a Dinosaur to have a name, health, and attack power.

E. (/10 points): As a developer, I want to instantiate three Robot objects and three Dinosaur objects and assign the appropriate values to all the objects.

-F. (/10 points): As a developer, I want the created Robot objects to be stored in a Fleet and the created Dinosaur objects to be stored in a Herd 
   (the Fleet and Herd must use a List to store the objects).

G. (/10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur and a Dinosaur to have the ability to attack a Robot on a Battlefield.

H. (/10 points): As a developer, I want a Robot/Dinosaur to lose health points (loss based on attack power) when another Robot/Dinosaur successfully attacks it.

I. (/10 points): As a developer, I want the battle to conclude once either all the robots in the Fleet have their health points reach zero or all 
   of the dinosaurs in the Herd have their health points reach zero.

Bonus points:

J. (/5 points): As a developer, I want a Robot to have the ability to choose from a List of different weapons that will be then assigned as its own weapon.

K  (/5 points): As a developer, I want a Dinosaur to have the ability to choose its attack name from a tuple of different attack names before attacking 
   a Robot in battle.

L.  (/2 points): As a developer, I want a Robot to have a power level and a Dinosaur to have an energy, which will decrease by 10 every time they attack.


'''

'''
my pseudo code from UML

class Robot:
    def __init__(self, name):
        self.name = 0
        self.health = 0
        self.weapon.addWeapon()

    def attack (self, dinosaur):
        void

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = ""
        self.health = 0
        self.attack_power = 0
    
    def attack (self, robot):
        void

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet (self):
        void

class Herd:
    def __init__(self):
        self.dinosaurs = []
    
    def create_herd (self):
        void

class Weapon:
    def __init__(self, name, attack_power):
        self.name = ""
        self.attack_power = 0

class Battlefield:
    def __init__(self):
        self.fleet.addFleet()
        self.herd.addHerd()

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

    def display_winner(self):
        void
  

'''
import random
from battlefield import Battlefield
from dinosaur import Dinosaur
from robot import Robot
from fleet import Fleet
from herd import Herd
import time


print("Dinodaur vs. Robot! Monster against Machine! Who will win!")
time.sleep(2)
# Dionosaur Fighters-------------------------------------------------------------------

trex = Dinosaur()
trex.dino_character("T-rex", 20, 100)
ankly = Dinosaur()
ankly.dino_character("Ankylosaurus", 10, 150)
utah = Dinosaur()
utah.dino_character("Utahraptor", 15, 125)


# Robot fighters-----------------------------------------------------------------
blades = Robot()
blades.robot_character("Blades", "saw blades", 20, 100)
laser = Robot()
laser.robot_character("Laser-bot", "lasers", 15, 125)
lava = Robot()
lava.robot_character("Lava-bot", "molten metal", 10, 150)

# Choosing fighters--------------------------------------------------------------
def choose_dino ():
    chosen = True
    print("Choose your dinosaur for battle!!!")
    time.sleep(1)
    print(f"(0) Name: {trex.name}, Attack Power: {trex.attack_power}, Health: {trex.health}")
    print(f"(1) Name: {ankly.name}, Attack Power: {ankly.attack_power}, Health: {ankly.health}")
    print(f"(2) Name: {utah.name}, Attack Power: {utah.attack_power}, Health: {utah.health}")
    while True:
        select_dino = int(input("Enter the number next to the robot you choose: "))
        if select_dino <= 2:
            if select_dino == 0:
                return trex
                chosen = False
            elif select_dino == 2: 
                return ankly
                chosen = False
            else:
                return utah
                chosen = False
        else:
            print("Try another selection")


def choose_robot ():
    chosen = True
    print("Choose your robot for battle!!!")
    time.sleep(1)
    print(f"(0) Name: {blades.name}, Weapon: {blades.weapon.name}, Attack Power: {blades.weapon.attack_power}, Health: {blades.health}")
    print(f"(1) Name: {laser.name}, Weapon: {laser.weapon.name}, Attack Power: {laser.weapon.attack_power}, Health: {laser.health}")
    print(f"(2) Name: {lava.name}, Weapon: {lava.weapon.name}, Attack Power: {lava.weapon.attack_power}, Health: {lava.health}")
    while True:
        select_robot = int(input("Enter the number next to the robot you choose: "))
        if select_robot <= 2:
            if select_robot == 0:
                return blades
                chosen = False
            elif select_robot == 2: 
                return lava
                chosen = False
            else:
                return laser
                chosen = False
        else:
            print("Try another selection")

robot_fighter = choose_robot()
dino_fighter = choose_dino()

# The random fight----------------------------------------------------------------------
battle = Battlefield()
victor = battle.random_battle(robot_fighter, dino_fighter)

print(victor, " is the victor!!!!")



'''
What is the task you are trying to accomplish? What is the goal? (answer below)
  
  
What do you think the problem or impediment is? (answer below)
 


What have you specifically tried in your code? (answer below)
    


What did you learn by dropping a breakpoint? (if unable to run your app due to error, please state that below in your answer)

'''
