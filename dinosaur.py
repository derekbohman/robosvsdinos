import random
class Dinosaur:
    def __init__(self, dinosaur_name, attack_power):
        self.dinosaur_name = dinosaur_name
        self.attack_power = attack_power
        self.health = 100
        self.dinosaur_attack_tuple = ("Bite", "Slash", "Tail Whip", "Stomp")
    
    def attack(self, robot):
        robot.health -= self.attack_power
        #print(f"{robot.robot_name} is being attacked by {self.dinosaur_name}, {self.dinosaur_name} did {self.attack_power} damage leaving {robot.robot_name} with {robot.health} remaining.")
        print(f"{self.dinosaur_name} attacked {robot.robot_name} with \"{self.dinosaur_attack_tuple[random.randint(0,3)]}\" for {self.attack_power} damage!")