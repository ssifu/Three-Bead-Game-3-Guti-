import pygame
from ThreeBeadGame.board import Board
from .constants import BLUE, RED, PINK

class Game:

    def __init__(self, window) -> None:
        self._init()
        self.window = window
    

    def update(self):
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
    
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = []

    def reset(self):
        self._init()
    
    def winner(self):
        return self.board.winner()
    
    def select(self, x, y):
        if self.selected:
            result = self._move(x, y)
            if not result:
                self.selected = None
                self.select(x, y)
        
        piece = self.board.get_piece(x, y)
        if type(piece) != tuple and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        
        return False
    
    def _move(self, x, y):
        piece = self.board.get_piece(x, y)
        if self.selected and piece != 0 and (x, y) in self.valid_moves:
            self.board.move(self.selected, x, y)
            self.change_turn()
        else:
            return False
        
        return True
    
    def draw_valid_moves(self, moves):
        for move in moves:
            x, y = move
            x_win, y_win = self.board.get_window_axis(x, y)
            pygame.draw.circle(self.window, BLUE, (x_win, y_win), radius=15)
    
    def change_turn(self):
        self.valid_moves = []
        if self.turn == RED:
            self.turn = PINK
        else:
            self.turn = RED

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()
