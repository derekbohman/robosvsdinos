from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.dinosaurs = []
    def create_herd(self):
        dinosaur_one = Dinosaur("Smaug", 20)
        dinosaur_two = Dinosaur("Little Foot", 10)
        dinosaur_three = Dinosaur("Godzilla", 30)
        self.dinosaurs.append(dinosaur_one, dinosaur_two, dinosaur_three)