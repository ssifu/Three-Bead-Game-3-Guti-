import pygame
from .constants import BLACK, RED, WHITE, GREY

class Piece:

    OUTLINE = 2
    
    def __init__(self, x_win, y_win, x_board, y_board, color) -> None:
        self.x_win = x_win
        self.y_win = y_win
        self.x_board = x_board
        self.y_board = y_board
        self.color = color

    def draw(self, win):
        radius = 15
        if self.color != None:
            pygame.draw.circle(win, BLACK, (self.x_win, self.y_win), radius=radius+self.OUTLINE)
            pygame.draw.circle(win, self.color, (self.x_win, self.y_win),  radius=radius)

    def move(self, x_win, y_win, x, y):
        self.x_win = x_win
        self.y_win = y_win
        self.x_board = x
        self.y_board = y

    def __repr__(self) -> str:
        return str(self.color)
