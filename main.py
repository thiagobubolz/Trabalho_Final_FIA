# -*- coding: utf-8 -*-

import board
import numpy



tabuleiro = board.Board()

lista = tabuleiro.calculate_verticals()
print("VERTICAIS")
print(lista)
print()

lista = tabuleiro.calculate_main_diagonals()
print("MAIN")
print(lista)
print()

lista = tabuleiro.calculate_secondary_diagonals()
print("SEC")
print(lista)
print()

