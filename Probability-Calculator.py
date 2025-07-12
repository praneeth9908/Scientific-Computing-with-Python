import copy
import random
from collections import Counter

class Hat:
    def __init__(self, **args):
        self.contents = []
        for key, value in args.items():
            self.contents.extend([key] * value)

    def __str__(self):
        return str(self.contents)
    
    def draw(self, num_balls_drawn):
        if num_balls_drawn > len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn
        
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(num_balls_drawn)]
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    experiment_success = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        counter = Counter(balls_drawn)
        is_valid =  all(counter.get(color,0) >= count for color, count in expected_balls.items())
        if is_valid:
            experiment_success += 1

    return experiment_success/num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={'red':2,'green':1}, num_balls_drawn=5,num_experiments=10)
print(probability)
