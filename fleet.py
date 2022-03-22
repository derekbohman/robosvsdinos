from robot import Robot
class Fleet:
    def __init__(self):
        self.robots = []
    def create_fleet(self):
        robot_one = Robot("T-800", 20)
        robot_two = Robot("Robo", 10)
        robot_three = Robot("Baymax", 30)
        self.robots.append(robot_one, robot_two, robot_three)