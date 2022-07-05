import pygame

from ThreeBeadGame.piece import Piece
from .constants import BLACK, ROWS, COLS, RED, WIDTH, HEIGHT, PINK, WHITE

class Board:

    def __init__(self) -> None:
        self.board = []
        self.selected_piece = None
        self.create_board()
    
    def draw_board(self, window):
        window.fill(WHITE)
        pygame.draw.rect(window, BLACK, pygame.Rect(10, 10, WIDTH-20, HEIGHT-20), 15)
        # Left Diagonal
        pygame.draw.line(window, BLACK, (20, 20), (580, 580), 20)
        # Top to Bottom
        pygame.draw.line(window, BLACK, (300, 20), (300, 580), 15)
        # Middle left to right
        pygame.draw.line(window, BLACK, (20, 300), (580, 300), 15)
        # Right Diagonal
        pygame.draw.line(window, BLACK, (580, 20), (20, 580), 20)

    def get_window_axis(self, x, y):
        if (x, y) == (0, 0):
            return 20, 20
        if (x, y) == (0, 1):
            return 300, 20
        if (x, y) == (0, 2):
            return 580, 20
        if (x, y) == (1, 0):
            return 20, 300
        if (x, y) == (1, 1):
            return 300, 300
        if (x, y) == (1, 2):
            return 580, 300
        if (x, y) == (2, 0):
            return 20, 580
        if (x, y) == (2, 1):
            return 300, 580
        if (x, y) == (2, 2):
            return 580, 580
    
    def evaluate(self):

        color = self.winner()
        if color == PINK:
            return 10
        elif color == RED:
            return -10
        return 0
    
    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if not isinstance(piece, tuple) and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, x, y):
        piece1 = self.board[x][y]
        self.board[piece.x_board][piece.y_board], self.board[x][y] = self.board[x][y], self.board[piece.x_board][piece.y_board]
        self.board[piece.x_board][piece.y_board] = piece.x_win, piece.y_win
        piece.move(piece1[0], piece1[1], x, y)

    def get_piece(self, x, y):
        return self.board[x][y]

    def create_board(self):
        # Human Player (RED)
        self.board.append(
            [
                Piece(20, 20, 0, 0, RED), 
                Piece(300, 20, 0, 1, RED), 
                Piece(580, 20, 0, 2, RED)
            ]
        )
        self.board.append(
            [
                (20, 300), 
                (300, 300), 
                (580, 300)
            ]
        )
        # AI Player (PINK)
        self.board.append(
            [
                Piece(20, 580, 2, 0, PINK), 
                Piece(300, 580, 2, 1, PINK), 
                Piece(580, 580, 2, 2, PINK)
            ]
        )
    
    def draw(self, window):
        self.draw_board(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if not isinstance(piece, tuple):
                    piece.draw(window)
    
    def winner(self):

        
        
        if type(self.board[0][0]) != tuple and type(self.board[0][1]) != tuple and type(self.board[0][2]) != tuple:
            if (self.board[0][0].color == self.board[0][1].color == self.board[0][2].color) and self.board[0][0].color == RED:
                return None
        
        if type(self.board[2][0]) != tuple and type(self.board[2][1]) != tuple and type(self.board[2][2]) != tuple:
            if (self.board[2][0].color == self.board[2][1].color == self.board[2][2].color) and self.board[2][0].color == PINK:
                return None

        # Checking rows
        for row in range(3):
            if type(self.board[row][0]) != tuple and type(self.board[row][1]) != tuple and type(self.board[row][2]) != tuple:
                if self.board[row][0].color == self.board[row][1].color == self.board[row][2].color:
                    # print(f"{self.board[row][0].color} won the game1")
                    return self.board[row][0].color
        
        # Checking columns
        for col in range(3):
            if type(self.board[0][col]) != tuple and type(self.board[1][col]) != tuple and type(self.board[2][col]) != tuple:
                if self.board[0][col].color == self.board[1][col].color == self.board[2][col].color:
                    # print(f"{self.board[0][col].color} won the game2")
                    return self.board[0][col].color
        
        # Checking diagonal1
        if type(self.board[0][0]) != tuple and type(self.board[1][1]) != tuple and type(self.board[2][2]) != tuple:
            if self.board[0][0].color == self.board[1][1].color == self.board[2][2].color:
                # print(f"{self.board[0][0].color} won the game3")
                return self.board[0][0].color
        
        # Checking diagonal2
        if type(self.board[0][2]) != tuple and type(self.board[1][1]) != tuple and type(self.board[2][0]) != tuple:
            if self.board[0][2].color == self.board[1][1].color == self.board[2][0].color:
                # print(f"{self.board[0][2].color} won the game4")
                return self.board[0][2].color
    
    def get_valid_moves(self, piece):
        empty_spots = []
        current_spot = piece.x_board, piece.y_board
    
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == dy == 0:
                    continue
                rangeX = range(0, 3)  # X bounds
                rangeY = range(0, 3)  # Y bounds
                
                (newX, newY) = (current_spot[0]+dx, current_spot[1]+dy)  # adjacent cell
                if current_spot == (0, 1) or current_spot == (2, 1):
                    if (newX, newY) == (1, 0):
                        continue
                    elif (newX, newY) == (1, 2):
                        continue
                if current_spot == (1, 0) or current_spot == (1, 2):
                    if (newX, newY) == (0, 1):
                        continue
                    elif (newX, newY) == (2, 1):
                        continue
                
                
                if (newX in rangeX) and (newY in rangeY) and (isinstance(self.board[newX][newY], tuple)):
                    empty_spots.append((newX, newY))

        return empty_spots

