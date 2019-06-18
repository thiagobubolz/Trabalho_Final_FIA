class Board():
    def __init__(self):
        self.board = \
                [[0,0,0,0,0,0]
                 [0,0,0,0,0,0,0]
                 [0,0,0,0,0,0,0,0]
                 [0,0,0,0,0,0,0,0,0]
                 [0,0,0,0,0,0,0,0,0,0]
                 [0,0,0,0,0,0,0,0,0,0]
                 [0,0,0,0,0,0,0,0,0]
                 [0,0,0,0,0,0,0,0]
                 [0,0,0,0,0,0,0]
                 [0,0,0,0,0,0]]
        self.score = 0

    def get_board(self):
        return self.board

    def get_score(self):
        return self.score

    def insert_move(self, posx, posy, player):
        self.board[posx][posy] = player

    def calculate_score(self):
        return self.score