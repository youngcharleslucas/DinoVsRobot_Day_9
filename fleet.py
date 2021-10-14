from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.robot_saw = Robot()
        self.robot_laser = Robot()
        self.robot_fire = Robot()
    
    def list_robots(self,name):
        self.robots.append(name)
        return self.robots
    
    def fleet (self):
        self.robot_saw.robot_character("Blades", "saw blades", 13, 100)
        self.robot_laser.robot_character("Laser-bot", "lasers", 16, 100)
        self.robot_fire.robot_character("Lava-bot", "molten metal", 19, 100)



    