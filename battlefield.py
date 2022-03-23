from fleet import Fleet
from herd import Herd
import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.display_welcome()

    def display_welcome(self):
        print("")
        print("Welcome to Dinosaurs vs. Robots")
        print("**************************************************")

    def run_game_dinosaurs(self):
        self.show_dinosaur_options()
        self.dinosaur_turn()
        self.battle()

    def run_game_robots(self):
        self.show_robot_options()
        self.robot_turn()
        self.battle()
        
    
    def dinosaur_turn(self):
        self.herd.dinosaurs[user_dinosaur_attack_choice].attack(self.fleet.robots[user_robot_defend_choice])
        if self.fleet.robots[user_robot_defend_choice].health <= 0:
            print("")
            print(f"*****{self.fleet.robots[user_robot_defend_choice].robot_name} has been destroyed!*****")
            del self.fleet.robots[user_robot_defend_choice]

    def robot_turn(self):
        self.fleet.robots[user_robot_attack_choice].attack(self.herd.dinosaurs[user_dinosaur_defend_choice])
        if self.herd.dinosaurs[user_dinosaur_defend_choice].health <= 0:
            print("")
            print(f"*****{self.herd.dinosaurs[user_dinosaur_defend_choice].dinosaur_name} has been slain!*****")
            del self.herd.dinosaurs[user_dinosaur_defend_choice]
              
    def show_dinosaur_options(self):
        print("")
        print("Current Dinosaur Herd:")
        print("")
        count = 0
        for dinosaur in self.herd.dinosaurs:
            print(f"Press {count} to select {dinosaur.dinosaur_name} ({dinosaur.health} health)")
            count += 1
        print("")
        global user_dinosaur_attack_choice 
        user_dinosaur_attack_choice = int(input("Which dinosaur would you like to attack with? "))
        print("")
        print("Current Robot Fleet:")
        print("")
        count = 0
        for robot in self.fleet.robots:
            print(f"Press {count} to select {robot.robot_name} ({robot.health} health")
            count += 1
        print("")
        global user_robot_defend_choice
        user_robot_defend_choice = int(input("Which robot would you like to attack? "))
        print("")
    
    def show_robot_options(self):
        print("")
        print("Current Robot Fleet:")
        print("")
        count = 0
        for robot in self.fleet.robots:
            print(f"Press {count} to select {robot.robot_name} ({robot.health} health")
            count += 1
        print("")
        global user_robot_attack_choice
        user_robot_attack_choice = int(input("Which robot would you like to attack with? "))
        print("")
        print("Current Dinosaur Herd:")
        print("")
        count = 0
        for dinosaur in self.herd.dinosaurs:
            print(f"Press {count} to select {dinosaur.dinosaur_name} ({dinosaur.health} health)")
            count += 1
        print("")
        global user_dinosaur_defend_choice 
        user_dinosaur_defend_choice = int(input("Which dinosaur would you like to attack? "))
        print("")

    def battle(self):
        global starting_team
        starting_team = random.randint(0,1)
        if len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:
            if starting_team == 0:
                self.run_game_dinosaurs()
            else:
                self.run_game_robots()
        else:
            self.display_winners()

    def display_winners(self):
        if len(self.herd.dinosaurs) == 0:
            print("")
            print("Robots win!!!")
        elif len(self.fleet.robots) == 0:
            print("")
            print("Dinosaurs win!!!")