from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.display_welcome()

    def display_welcome(self):
        print("")
        print("Welcome to Dinosaurs vs. Robots")
        print("**************************************************")

    def run_game(self):
        self.dinosaur_turn()
        self.robot_turn()
        self.battle()
    
    def dinosaur_turn(self):
        self.show_dinosaur_options()
        user_dinosaur_choice = int(input("Which dinosaur would you like to attack with? "))
        self.herd.dinosaurs[user_dinosaur_choice].attack(self.fleet.robots[0])
        if self.fleet.robots[0].health <= 0:
            del self.fleet.robots[0]

    def robot_turn(self):
        self.show_robot_options()
        user_robot_choice = int(input("Which robot would you like to attack with? "))
        self.fleet.robots[user_robot_choice].attack(self.herd.dinosaurs[0])
        if self.herd.dinosaurs[0].health <= 0:
            del self.herd.dinosaurs[0]
              
    def show_dinosaur_options(self):
        print("")
        print("Current Dinosaur Herd:")
        count = 0
        for dinosaur in self.herd.dinosaurs:
            print(f"Press {count} to select {dinosaur.dinosaur_name} ({dinosaur.health} health)")
            count += 1
    
    def show_robot_options(self):
        print("")
        print("Current Robot Fleet:")
        count = 0
        for robot in self.fleet.robots:
            print(f"Press {count} to select {robot.robot_name} ({robot.health} health")
            count += 1
    
    def battle(self):
        if len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:
            self.run_game()
        else:
            self.display_winners()

    def display_winners(self):
        if len(self.herd.dinosaurs) == 0:
            print("Robots win!!!")
        elif len(self.fleet.robots) == 0:
            print("Dinosaurs win!!!")