# -*- coding: utf-8 -*-

import board


def get_possible_moves(board):
    moves = []
    i = 0
    j = 0
    for line in board:
        for item in line:
            if item == 0:
                moves.append([i,j])
            j = j + 1
        i = i + 1
    return moves


def make_move(board, move, player):
    board[int(move[0])][int(move[1])] = player
    return board

