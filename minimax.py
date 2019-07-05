# -*- coding: utf-8 -*-

import utils
import copy
from math import inf

def minimax(tabuleiro, depth, alphabeta, maximizingPlayer, current_move, player):
    best_move = current_move
    score = tabuleiro.calculate_board_score(player)

    if depth == 0 or score == inf:
        return score, current_move

    possible_moves = utils.get_possible_moves(tabuleiro.get_board())

    if maximizingPlayer:
        maxEval = -inf
        for move in possible_moves:
            evalue, pos = minimax(utils.make_move(copy.deepcopy(tabuleiro), move, 1), depth-1, alphabeta, False, move, player)
            if maxEval < evalue:
                maxEval = evalue
                best_move = move
            alphabeta[0] = max(alphabeta[0], evalue)
            if alphabeta[1] <= alphabeta[0]:
                break

        return maxEval, best_move
    else:
        minEval = inf
        for move in possible_moves:
            evalue, pos = minimax(utils.make_move(copy.deepcopy(tabuleiro), move, 2), depth - 1, alphabeta, True, move, player)
            if minEval > evalue:
                minEval = evalue
                best_move = move
            alphabeta[1] = min(alphabeta[1], evalue)
            if alphabeta[1] <= alphabeta[0]:
                break

        return minEval, best_move