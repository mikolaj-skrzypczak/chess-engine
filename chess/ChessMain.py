'''
Main driver file.
Handling user input.
Displaying current GameStatus object.
'''

import pygame as p
from chess import ChessEngine
import sys

WIDTH = HEIGHT = 512
DIMENSION = 8

SQUARE_SIZE = HEIGHT // DIMENSION

MAX_FPS = 15

IMAGES = {}

'''
Initialize a global directory of images.
This will be called exactly once in the main.
'''

def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB' ,'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQUARE_SIZE,SQUARE_SIZE))
        
        
'''
The main driver for our code.
This will handle user input and updating the graphics.
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    game_state = ChessEngine.GameState()
    loadImages() #do this only once before while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
                p.quit()
                sys.exit()
        
        clock.tick(MAX_FPS)
        p.display.flip()
        drawGameState(screen, game_state)


'''
Responsible for all the graphics within current game state.
'''
def drawGameState(screen, game_state):
    drawBoard(screen) #draw squares on the board
    #add in piece highlighting or move suggestions (later)
    drawPieces(screen, game_state.board) #draw pieces on top of those squares      

'''
Draw the squares on the board.
The top left square is always light.
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row+column) % 2)]
            p.draw.rect(screen, color, p.Rect(column*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
'''
Draw the pieces on the board using the current game_state.board
'''
def drawPieces(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(column*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
         
                
if __name__ == "__main__":
    main()
