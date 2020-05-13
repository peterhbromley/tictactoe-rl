PLAYER_X = 1 
PLAYER_O = -1 
class Game:
    def __init__(self, board, player_x, player_o):
        self.board = board
        self.players = {
            PLAYER_X: player_x,
            PLAYER_O: player_o,
        }

    def play(self):
        while not self.board.game_over:
            player = self.players[self.board.turn]
            move = player.move(self.board.state)

            self.board.place(move)
        
        return self.board.check_win()
