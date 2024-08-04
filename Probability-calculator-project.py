import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = [k for k, v in kwargs.items() for _ in range(v)]

    def draw(self,  n_balls: int):
        drawn = []
        if (n_balls >= len(self.contents)):
            drawn = self.contents
            self.contents = []
        else:
            for _ in range(n_balls):
                index = random.randrange(len(self.contents))
                drawn.append(self.contents[index])
                self.contents[index] = self.contents[-1]
                self.contents.pop()
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        m += 1 if balls_req == len(expected_balls) else 0

    return m / num_experiments