from weapon import Weapon
from dinosaur import Dinosaur
class Robot:
    def __init__(self, robot_name):
        self.robot_name = robot_name
        self.health = 100
        self.weapon = Weapon

    def attack(self, dinosaur):
        pass