from copy import deepcopy
import pygame

RED = (255, 0, 0)
PINK = (255, 192, 203)

def minimax(position, depth, max_player, game):

    if depth == 0 or position.winner() != None:
        return position.evaluate()-depth, position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, PINK, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move

def simulate_moves(piece, move, board, game):
    board.move(piece, move[0], move[1])
    return board

def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move in valid_moves:
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.x_board, piece.y_board)
            new_board = simulate_moves(temp_piece, move, temp_board, game)
            moves.append(new_board)

    return moves
