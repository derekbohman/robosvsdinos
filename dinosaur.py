import random

class Dinosaur:
    def __init__(self, dinosaur_name, attack_power):
        self.dinosaur_name = dinosaur_name
        self.attack_power = attack_power
        self.health = 100
        self.dinosaur_attack_tuple = ("Bite", "Slash", "Tail Whip", "Stomp")
        self.energy = 50
    
    def attack(self, robot):
        robot.health -= self.attack_power
        self.energy -=10
        print(f"{self.dinosaur_name} attacked {robot.robot_name} with \"{self.dinosaur_attack_tuple[random.randint(0,3)]}\" for {self.attack_power} damage!")