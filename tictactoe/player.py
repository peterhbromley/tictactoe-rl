import numpy as np
from numpy.random import choice, randint


EMPTY = 0 

class Player:
    def move(self, state):
        raise NotImplementedError("Subclasses of Player need a `move` method")


class RandomPlayer(Player):
    def move(self, state):
        return randint(9)


class ValidRandomPlayer(Player):
    def move(self, state):
        return choice(np.flatnonzero(state == EMPTY))


class HumanPlayer(Player):
    def move(self, state):
        loc = input('Enter move: ')
        return int(loc)
