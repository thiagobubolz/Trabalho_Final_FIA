from itertools import groupby
from math import inf
import utils

class Board:
    def __init__(self):
        self.board = [[0, 0, 1, 1, 0],
                      [0, 0, 2, 0, 0, 0],
                      [0, 0, 2, 0, 0, 0, 0],
                      [0, 2, 0, 0, 0, 0, 0, 0],
                      [0, 2, 2, 2, 0, 2, 0, 0, 0],
                      [1, 1, 1, 1, 0, 2, 2, 2, 2, 0],
                      [1, 0, 1, 0, 0, 1, 1, 0, 0],
                      [0, 2, 0, 0, 2, 0, 0, 0],
                      [0, 0, 0, 0, 0, 2, 0],
                      [1, 1, 0, 1, 0, 0],
                      [0, 2, 0, 0, 0]]


    def get_board(self):
        return self.board

    def insert_move(self, posx, posy, player):
        self.board[posx][posy] = player

    def calculate_board_score(self, player):
        if player == 1:
            verticals_p1 = self.calculate_verticals(1)
            m_diagonals_p1 = self.calculate_main_diagonals(utils.main_diagonals, 1)
            s_diagonals_p1 = self.calculate_secondary_diagonals(utils.secondary_diagonals, 1)

            verticals_p2 = self.calculate_verticals(2) * (-1)
            m_diagonals_p2 = self.calculate_main_diagonals(utils.main_diagonals, 2) * (-1)
            s_diagonals_p2 = self.calculate_secondary_diagonals(utils.secondary_diagonals, 2) * (-1)

        else :
            verticals_p1 = self.calculate_verticals(2)
            m_diagonals_p1 = self.calculate_main_diagonals(utils.main_diagonals, 2)
            s_diagonals_p1 = self.calculate_secondary_diagonals(utils.secondary_diagonals, 2)

            verticals_p2 = self.calculate_verticals(1) * (-1)
            m_diagonals_p2 = self.calculate_main_diagonals(utils.main_diagonals, 1) * (-1)
            s_diagonals_p2 = self.calculate_secondary_diagonals(utils.secondary_diagonals, 1) * (-1)

        '''
        empty_verticals = self.calculate_verticals(0)
        empty_m_diagonals_p1 = self.calculate_main_diagonals(0)
        empty_s_diagonals_p1 = self.calculate_secondary_diagonals(0)
        self.set_score(verticals_p1 + verticals_p2 + empty_verticals + m_diagonals_p1 + m_diagonals_p2 + empty_m_diagonals_p1 + s_diagonals_p1 + s_diagonals_p2 + empty_s_diagonals_p1)
        '''

        return verticals_p1 + verticals_p2 + m_diagonals_p1 + m_diagonals_p2 + s_diagonals_p1 + s_diagonals_p2


    def calculate_main_diagonals(self, main_diagonals, player):
        compara = []
        lista = []
        string = []
        for line in main_diagonals:
            for item in line:
                compara.append(self.board[item[0]][item[1]])
            lista.append([len(list(g[1])) for g in groupby(compara) if g[0] == player])
            string.append(str(compara))
            compara = []
        #print(lista)
        soma = 0
        for line in lista:
            for item in line:
                if item == 1:
                    soma += 0
                elif item == 2:
                    soma += 35
                elif item == 3:
                    soma += 120
                elif item == 4:
                    soma += 600
                elif item >= 5:
                    soma = inf

        if player != 1:
       		for s in string:
        		if(s.find('0, 2, 2, 2, 0') != -1):
        			soma = soma + 1800
        		elif(s.find('0, 2, 2, 2, 2, 0') != -1):
        			soma = soma + 6000 
        return soma

    def calculate_secondary_diagonals(self, secondary_diagonals, player):
        compara = []
        lista = []
        string = []
        for line in secondary_diagonals:
            for item in line:
                compara.append(self.board[item[0]][item[1]])
            lista.append([len(list(g[1])) for g in groupby(compara) if g[0] == player])
            string.append(str(compara))
            compara = []
        #print(lista)
        soma = 0
        for line in lista:
            for item in line:
                if item == 1:
                    soma += 0
                elif item == 2:
                    soma += 35
                elif item == 3:
                    soma += 120
                elif item == 4:
                    soma += 600
                elif item >= 5:
                    soma = inf

        if player != 1:
       		for s in string:
        		if(s.find('0, 2, 2, 2, 0') != -1):
        			soma = soma + 1800
        		elif(s.find('0, 2, 2, 2, 2, 0') != -1):
        			soma = soma + 6000          
        return soma

    def calculate_verticals(self, player):
        lista = []
        string = []
        for i in range(9):
            lista.append([len(list(g[1])) for g in groupby(self.board[i]) if g[0] == player])
            string.append(str(self.board[i]))
        soma = 0
        #print(lista)
        for line in lista:
            for item in line:
                if item == 1:
                    soma += 0
                elif item == 2:
                    soma += 35
                elif item == 3:
                    soma += 120
                elif item == 4:
                    soma += 600
                elif item >= 5:
                    soma = inf
        if player != 1:
       		for s in string:
        		if(s.find('0, 2, 2, 2, 0') != -1):
        			soma = soma + 1800
        		elif(s.find('0, 2, 2, 2, 2, 0') != -1):
        			soma = soma + 6000 

        return soma
