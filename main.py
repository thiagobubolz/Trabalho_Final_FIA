# -*- coding: utf-8 -*-

import board
import utils

tabuleiro = board.Board()

lista = tabuleiro.calculate_board_score()

print(lista)

moves = utils.get_possible_moves(tabuleiro.board)

print(moves)