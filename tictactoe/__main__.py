from .board import Board
from .game import Game
from .player import (
    HumanPlayer,
    RandomPlayer,
    ValidRandomPlayer,
)


def main():
    wins = {0: 0, -1: 0, 1: 0}
    for _ in range(10000):
        board = Board.empty()
        game = Game(board, ValidRandomPlayer(), ValidRandomPlayer())
        winner = game.play()
        wins[winner] += 1 
    print(wins)

if __name__ == '__main__':
    main()
