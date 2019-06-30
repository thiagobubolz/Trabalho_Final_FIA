# -*- coding: utf-8 -*-

import board
import utils
from math import inf
import minimax


tabuleiro = board.Board()

lista = tabuleiro.calculate_board_score()

#print(lista)

moves = utils.get_possible_moves(tabuleiro.get_board())

print(moves)

score, move = minimax.minimax(tabuleiro, 3, -inf, inf, True, [0,0])

print("SCORE: ")
print(score)
print("Movimento")
print(move)
