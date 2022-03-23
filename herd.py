from dinosaur import Dinosaur
import random

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()
    
    def create_herd(self):
        dinosaur_one = Dinosaur("Smaug", random.randint(25,50))
        dinosaur_two = Dinosaur("Little Foot", random.randint(25,50))
        dinosaur_three = Dinosaur("Godzilla", random.randint(25,50))
        self.dinosaurs.append(dinosaur_one)
        self.dinosaurs.append(dinosaur_two)
        self.dinosaurs.append(dinosaur_three)