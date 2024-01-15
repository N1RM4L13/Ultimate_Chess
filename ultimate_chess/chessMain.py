"""
Main driver file responsible for handling user input and displaying current GameState object
"""

import pygame as p
from ultimate_chess import chessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
Initializing a global dictionary of images.
'''


def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


'''
Handles user input and updates the graphics
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    game_state = chessEngine.GameState()
    loadImages()
    running = True
    sqSelected=()
    playerClicks=[]
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col, row = location[0]//SQ_SIZE, location[1]//SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected, playerClicks = (), []
                else:
                    sqSelected= (row,col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    move = chessEngine.Move()
                    print(move.getChessNotation())
                    game_state.makeMove(move)
                    sqSelected=()
                    playerClicks =[]




        drawGameState(screen, game_state)
        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen, game_state):
    drawBoard(screen)
    drawPieces(screen, game_state.board)


def drawBoard(screen):
    colors = [p.Color("lightgrey"), p.Color("darkgreen")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))



if __name__ == "__main__":
    main()
