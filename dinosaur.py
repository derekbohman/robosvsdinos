class Dinosaur:
    def __init__(self, dinosaur_name, attack_power):
        self.dinosaur_name = dinosaur_name
        self.attack_power = attack_power
        self.health = 100
    
    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{robot.robot_name} is being attacked by {self.dinosaur_name}, {self.dinosaur_name} did {self.attack_power} damage leaving {robot.robot_name} with {robot.health} remaining.")