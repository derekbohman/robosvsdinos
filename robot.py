from weapon import Weapon
import random

class Robot:
    def __init__(self, robot_name):
        robot_weapons = ["Punch", "Kick", "Shoulder Smash", "Headbutt"]
        self.robot_name = robot_name
        self.health = 100
        self.weapon = Weapon(robot_weapons[random.randint(0,1)], random.randint(25,50))

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        #print(f"{dinosaur.dinosaur_name} is being attacked by {self.robot_name}, {self.robot_name} did {self.weapon.attack_power} damage leaving {dinosaur.dinosaur_name} with {dinosaur.health} remaining.")
        print(f"{self.robot_name} attacked {dinosaur.dinosaur_name} with \"{self.weapon.weapon_name}\" for {self.weapon.attack_power} damage!")