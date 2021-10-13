from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet (self):
        void

robot_saw = Robot()
robot_saw.name("Blade")
robot_saw.weapon.name("Saw blades")
robot_saw.weapon.attack_power(13)

robot_laser = Robot()
robot_laser.name("Laser")