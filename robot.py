from weapon import Weapon

class Robot:
    def __init__(self, robot_name):
        self.robot_name = robot_name
        self.health = 100
        self.weapon = Weapon("Mace", 50)
    
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f"{dinosaur.dinosaur_name} is being attacked by {self.robot_name}, {self.robot_name} did {self.weapon.attack_power} damage leaving {dinosaur.dinosaur_name} with {dinosaur.health} remaining.")