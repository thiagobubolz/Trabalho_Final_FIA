import urllib.request
import sys
import random
import time
import minimax_sem_poda
import board
from math import inf
import utils
import copy
import datetime

start = 0.0
end = 0.0


if len(sys.argv) == 1:
    print("Voce deve especificar o numero do jogador (1 ou 2)\n\nExemplo:    ./random_client.py 1")
    quit()

# Alterar se utilizar outro host
host = "http://localhost:8080"

player = int(sys.argv[1])

# Reinicia o tabuleiro
resp = urllib.request.urlopen("%s/reiniciar" % host)

done = False
while not done:
    # Pergunta quem eh o jogador
    resp = urllib.request.urlopen("%s/jogador" % host)
    player_turn = int(resp.read())

    # Se jogador == 0, o jogo acabou e o cliente perdeu
    if player_turn == 0:
        print("I lose.")
        done = True

    # Se for a vez do jogador
    if player_turn == player:

        start = datetime.datetime.now()

        # Pega o tabuleiro
        resp = urllib.request.urlopen("%s/tabuleiro" % host)
        movimentos = eval(resp.read())
        tabuleiro = board.Board()
        tabuleiro.board = movimentos

        #pega movimento aleatorio para inicial
        resp = urllib.request.urlopen("%s/movimentos" % host)
        movimentos = eval(resp.read())
        inicial_move = random.choice(movimentos)
        inicial_move = list(inicial_move)
        inicial_move[0] = inicial_move[0] - 1
        inicial_move[1] = inicial_move[1] - 1

        print(inicial_move)

        # Escolhe um movimento
        score, move = minimax_sem_poda.minimax(tabuleiro, 2, True, inicial_move, 1)
        end = datetime.datetime.now()

        # Executa o movimento
        print("Movimento Escolhido: " + str(move[0]+1) + "," + str(move[1]+1))
        diff = end - start
        print("Time H:M:S\t" + str(diff))
        resp = urllib.request.urlopen(
            "%s/move?player=%d&coluna=%d&linha=%d" % (host, player, move[0]+1, move[1]+1))
        msg = eval(resp.read())

        # Se com o movimento o jogo acabou, o cliente venceu
        if msg[0] == 0:
            print("I win")
            done = True
        #Se for um sanduiche entra aqui
        elif msg[0] == 2:
            # Pega os movimentos possiveis
            resp = urllib.request.urlopen("%s/movimentos" % host)
            movimentos = eval(resp.read())
            # Escolhe um movimento aleatoriamente
            movimento = random.choice(movimentos)
            # Executa o movimento
            resp = urllib.request.urlopen(
                "%s/move?player=%d&coluna=%d&linha=%d" % (host, player, movimento[0], movimento[1]))
            msg = eval(resp.read())
        elif msg[0] < 0:
            if msg[0] == -5:
                print("movimento invalido")
                tab2 = copy.deepcopy(tabuleiro)
                tab2 = utils.make_move(tab2, move, -1)
                # Escolhe um movimento
                score, move = minimax_sem_poda.minimax(tab2, 2, True, inicial_move, 1)
                # Executa o movimento
                print("Movimento Escolhido: " + str(move[0] + 1) + "," + str(move[1] + 1))
                end = datetime.datetime.now()
                diff = end - start
                print("Time H:M:S\t" + str(diff))
                resp = urllib.request.urlopen(
                    "%s/move?player=%d&coluna=%d&linha=%d" % (host, player, move[0] + 1, move[1] + 1))
            else:
                raise Exception(msg[1])

    # Descansa um pouco para nao inundar o servidor com requisicoes
    time.sleep(1)




