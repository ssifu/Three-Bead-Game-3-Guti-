import time
import pygame
from ThreeBeadGame.constants import PINK, WIDTH, HEIGHT, RED, WHITE
from ThreeBeadGame.game import Game
from Minimax.minimax import minimax
from Minimax.minimax import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Three Bead Game")

def get_x_y_from_mouse(pos):
    mouse_x, mouse_y = pos
    x, y = -1, -1
    if mouse_x in range(10, 10+30) and mouse_y in range(10, 10+30):
        x , y = 0, 0
    elif mouse_x in range(300-30, 300+30) and mouse_y in range(20-10, 20+30):
        x, y = 0, 1
    elif mouse_x in range(580-30, 580+30) and mouse_y in range(20-10, 20+30):
        x, y = 0, 2
    elif mouse_x in range(20-10, 20+30) and mouse_y in range(300-30, 300+30):
        x, y = 1, 0
    elif mouse_x in range(300-30, 300+30) and mouse_y in range(300-30, 300+30):
        x, y = 1, 1
    elif mouse_x in range(580-30, 580+30) and mouse_y in range(300-30, 300+30):
        x, y = 1, 2
    elif mouse_x in range(20-10, 20+30) and mouse_y in range(580-30, 580+30):
        x, y = 2, 0
    elif mouse_x in range(300-30, 300+30) and mouse_y in range(580-30, 580+30):
        x, y = 2, 1
    elif mouse_x in range(580-30, 580+30) and mouse_y in range(580-30, 580+30):
        x, y = 2, 2
    
    return x, y

def main():
    run = True
    # To run the game at a constant frame rate
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == PINK:
            _, new_board = minimax(game.get_board(), depth=6, max_player=PINK, game=game)
            game.ai_move(new_board)

        if game.winner() != None:
            if game.winner() == (255, 255, 255):
                print(f"{PINK} won the game")
            if game.winner() == (255, 0, 0):
                print(f"{RED} won the game")
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x_board, y_board = get_x_y_from_mouse(pos)
                if not (0 <= x_board <= 2) and (0 <= y_board <= 2):
                    x_board, y_board = get_x_y_from_mouse(pos)
                game.select(x_board, y_board) 

        
        game.update()
    
    time.sleep(1)
    pygame.quit()

main()
