# --------
# @file     pneuma_class.py
# @author   Jordan Reed
# @date     12/11/25
# @brief    the pneuma class. mnages the levels and points
# ---------

from math import sqrt

class Pneuma:
    def __init__(self, points=0, level=1):
        self.pneuma_points = points
        self.pneuma_level = level

        self.update_pneuma_level()
    
    def update_pneuma_level(self):
        level = (-5 + sqrt(25+2*self.pneuma_points))/10
        self.pneuma_level = int(level) + 1
    
    def print_pneuma(self):
        print(f'\nStatus')
        print(f'------')
        print(f'pneuma points: {self.pneuma_points}')
        print(f'pneuma level: {self.pneuma_level}')

    def add_points(self, points):
        self.pneuma_points += points
        self.update_pneuma_level()
    
    def remove_points(self, points):
        self.pneuma_points -= points
        
        if self.pneuma_points < 0:
            self.pneuma_points = 0

        self.update_pneuma_level()

if __name__ == "__main__":
    print("Testing pneuma class")

    p = Pneuma()

    p.add_points(100)
    p.print_pneuma()

    p.remove_points(10)
    p.print_pneuma()

    p.add_points(500)
    p.print_pneuma()

    p.remove_points(1000)
    p.print_pneuma()