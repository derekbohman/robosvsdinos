from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet() #Not sure if this is correct.
        self.herd = Herd() #Not sure if this is correct.
    def run_game(self):
        self.display_welcome()
    def display_welcome(self):
        print("")
        print("Welcome to Dinos vs. Robos")
        print("")
    def battle(self): #Does this represent the actual fighting or does it represent choosing options like who to attack?
        pass
    def dino_turn(self, dinosaur):
        pass
    def robo_turn(self, robot):
        pass
    def show_dino_opponent_options(self):
        pass
    def show_robo_opponent_options(self):
        pass
    def display_winners(self):
        pass