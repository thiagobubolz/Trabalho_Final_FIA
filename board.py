from itertools import groupby


class Board:
    def __init__(self):
        self.board = [[0, 0, 1, 1, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                      [1, 0, 1, 1, 0, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [1, 1, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0]]
        self.score = 0
        self.main_diagonals = [[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]],
                               [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 0]],
                               [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 1], [7, 0]],
                               [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 2], [7, 1], [8, 0]],
                               [[0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1], [9, 0]],
                               [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1], [10, 0]],
                               [[2, 6], [3, 6], [4, 6], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],
                               [[3, 7], [4, 7], [5, 7], [6, 6], [7, 5], [8, 4], [9, 3], [10, 2]],
                               [[4, 8], [5, 8], [6, 7], [7, 6], [8, 5], [9, 4], [10, 3]],
                               [[5, 9], [6, 8], [7, 7], [8, 6], [9, 5], [10, 4]]]

        self.secondary_diagonals = [[[5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]],
                                    [[4, 0], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],
                                    [[3, 0], [4, 1], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],
                                    [[2, 0], [3, 1], [4, 2], [5, 3], [6, 3], [7, 3], [8, 3], [9, 3], [10, 3]],
                                    [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4], [10, 4]],
                                    [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5]],
                                    [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 6], [7, 6], [8, 6]],
                                    [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 7], [7, 7]],
                                    [[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 8]],
                                    [[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]]

    def get_board(self):
        return self.board

    def get_score(self):
        return self.score

    def insert_move(self, posx, posy, player):
        self.board[posx][posy] = player

    def calculate_score(self):
        return self.score

    def calculate_main_diagonals(self):
        compara = []
        lista = []
        for line in self.main_diagonals:
            for item in line:
                compara.append(self.board[item[0]][item[1]])
            lista.append([len(list(g[1])) for g in groupby(compara) if g[0] == 1])
            compara = []
        return lista

    def calculate_secondary_diagonals(self):
        compara = []
        lista = []
        for line in self.secondary_diagonals:
            for item in line:
                compara.append(self.board[item[0]][item[1]])
            lista.append([len(list(g[1])) for g in groupby(compara) if g[0] == 1])
            compara = []
        return lista

    def calculate_verticals(self):
        lista = []
        for i in range(9):
            lista.append([len(list(g[1])) for g in groupby(self.board[i]) if g[0] == 1])

        return lista
