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
    
    def create_fleet (self):
        void

    def saw_robot(self):
        self.robot_saw.set_name("Blades")
        self.robot_saw.weapon.set_name("saw blades")
        self.robot_saw.weapon.set_power(13)
        self.robots.append(self.robot_saw.name)

    def laser_robot(self):
        self.robot_laser.set_name("Laser-bot")
        self.robot_laser.weapon.set_name("lasers")
        self.robot_laser.weapon.set_power(16)

    def fire_robot(self):
        self.robot_fire.set_name("Lava-bot")
        self.robot_fire.weapon.set_name("molten metal")
        self.robot_fire.weapon.set_power(19)

    