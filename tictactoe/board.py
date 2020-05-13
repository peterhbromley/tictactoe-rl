import numpy as np


X = 1 
O = -1 
EMPTY = 0 

class Board:
    def __init__(self, state, turn):
        self.state = state 
        self.turn = turn

    @classmethod
    def empty(cls):
        state = np.zeros(9, dtype=int)
        return cls(state, X)
    
    @property
    def markers(self):
        return {
            X: 'X',
            O: 'O',
            EMPTY: ' ',
        }

    @property
    def piece(self):
        return self.markers[self.turn]

    def valid_move(self, move):
        return self.state[move] == EMPTY

    def print(self):
        print("Tic Tac Toe")
        print("-----------")
        board = self.state.reshape(3, 3)
        for i in range(3):
            print("  ", end='|')
            for j in range(3):
                loc = i * 3 + j
                print(self.markers[self.state[loc]], end='|')
            print('')
        print('-----------')
        print(f"Player {self.piece}'s turn")

    def change_turn(self):
        self.turn *= -1 
        
    def check_win(self):
        grid = self.state.reshape(3, 3)
        for player in [X, O]:
            placed = (grid == player)
            win = placed.all(0).any() | placed.all(1).any()
            win |= np.diag(placed).all() | np.diag(placed[:, ::-1]).all()

            if win:
                return player

        return EMPTY

    @property
    def board_full(self):
        return (self.state != EMPTY).all()

    @property
    def game_over(self):
        return self.board_full or (self.check_win() != EMPTY)

    def place(self, loc):
        """
        Place the piece of `self.turn` at `loc`. If `loc` is already
        taken, the turn is lost.

        0|1|2
        3|4|5
        6|7|8

        Parameters
        ----------
        loc : int
            The location to place a piece.
        """
        if self.valid_move(loc):
            self.state[loc] = self.turn
        
        self.change_turn()

    
