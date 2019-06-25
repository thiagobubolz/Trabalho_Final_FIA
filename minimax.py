# -*- coding: utf-8 -*-

import board

def minimax(board, possible_moves, player):
    scores = []
    for move in possible_moves:
        