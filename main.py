






function minimax(position, depth, maximizingPlayer)
	if depth == 0 or game over in position
		return static evaluation of position

	if maximizingPlayer
		maxEval = -infinity
		for each child of position
			eval = minimax(child, depth - 1, false)
			maxEval = max(maxEval, eval)
		return maxEval

	else
		minEval = +infinity
		for each child of position
			eval = minimax(child, depth - 1, true)
			minEval = min(minEval, eval)
		return minEval


// initial call
minimax(currentPosition, 3, true)

# -*- coding: utf-8 -*-

import board
import utils

tabuleiro = board.Board(0)

lista = tabuleiro.calculate_board_score()

print(lista)

moves = utils.get_possible_moves(tabuleiro.board)

print(moves)