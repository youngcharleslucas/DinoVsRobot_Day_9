from robot import Robot

class Fleet:
    def __init__(self):
        self.robot_saw = Robot()
        self.robot_laser = Robot()
        self.robot_fire = Robot()


    def saw_robot(self):
        self.robot_saw.set_name("Blades")
        self.robot_saw.set_weapon_name("saw blades")
        self.robot_saw.set_weapon_power(13)
        self.robot_saw.set_health(100)


        # self.robot_saw.robot_character("Blades", "saw blades", 13, 100)
        # self.robot_laser.robot_character("Laser-bot", "lasers", 16, 100)
        # self.robot_fire.robot_character("Lava-bot", "molten metal", 19, 100)


    