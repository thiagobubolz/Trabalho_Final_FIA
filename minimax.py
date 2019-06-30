# -*- coding: utf-8 -*-

import board
import utils
import copy
from math import inf

def minimax(board, depth, maximizingPlayer, last_move):
    possible_moves = utils.get_possible_moves(board)
    score = board.calculate_board_score()

    if depth == 0:
        return 0

    if maximizingPlayer:
        maxEval = -inf
        for move in possible_moves:
            evalue, pos = minimax(utils.make_move(copy.deepcopy(board.get_board()), move, 1), depth-1, False)
            if maxEval > evalue:


        return

    if score == 5000000:
        return movimento, score

    for move in possible_moves:
        aux = utils.make_move(copy.deepcopy(board.get_board()), move, player)
        aux.

        if player == 1:
            next_player = 2
        else:
            next_player = 1

        minimax(aux, next_player)

        scores.append(aux.calculate_board_score())
        movimentos.append(move)

    if player == 1:
        score = max(scores)


    return movimento, score