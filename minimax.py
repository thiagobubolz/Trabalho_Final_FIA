# -*- coding: utf-8 -*-

import utils
import copy
from math import inf

def minimax(tabuleiro, depth, maximizingPlayer, current_move):
    score = tabuleiro.calculate_board_score()

    if depth == 0 or score == inf:
        return score, current_move

    possible_moves = utils.get_possible_moves(tabuleiro.get_board())

    if maximizingPlayer:
        maxEval = -inf
        for move in possible_moves:
            evalue, pos = minimax(utils.make_move(copy.deepcopy(tabuleiro), move, 1), depth-1, False, move)
            if maxEval < evalue:
                maxEval = evalue
                best_move = move

        return maxEval, best_move
    else:
        minEval = inf
        for move in possible_moves:
            evalue, pos = minimax(utils.make_move(copy.deepcopy(tabuleiro), move, 2), depth - 1, True, move)
            if minEval > evalue:
                minEval = evalue
                best_move = move

        return minEval, best_move