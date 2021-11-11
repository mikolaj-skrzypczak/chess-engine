import pygame as p
import csv
import numpy as np

BOARD_WIDTH = BOARD_HEIGHT = 512
DIMENSION = 8
SQUARE_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}
BOARD = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
         ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
         ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

ALL_PIECES = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR", "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR",
              "bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp", "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
ONLY_FIGURES = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR",
                "wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"]
ONLY_PAWNS = ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp",
              "wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"]


def gen_board(pieces):
    board = [["--" for _ in range(8)] for _ in range(8)]
    for piece in pieces:
        x = np.random.randint(low=0, high=8)
        y = np.random.randint(low=0, high=8)
        while board[x][y] != '--':
            x = np.random.randint(low=0, high=8)
            y = np.random.randint(low=0, high=8)
        board[x][y] = piece
    return board


def create_board_with_pieces_save_increment_counter(pieces, screen, counter):
    board = gen_board(pieces)
    drawGameState(screen, board)
    p.image.save(screen, f'images/board{to_string_helper(counter)}.png')
    save_to_csv(f"matrices/board{to_string_helper(counter)}.csv", board)
    counter += 1
    return counter


def create_board_with_random_pieces_save_increment_counter(n_pieces, screen, counter):
    pieces = np.random.choice(ALL_PIECES, n_pieces)
    board = gen_board(pieces)
    drawGameState(screen, board)
    p.image.save(screen, f'images/board{to_string_helper(counter)}.png')
    save_to_csv(f"matrices/board{to_string_helper(counter)}.csv", board)
    counter += 1
    return counter


def to_string_helper(counter):
    str_counter = str(counter)
    if len(str_counter) == 1:
        str_counter = "000" + str_counter
    elif len(str_counter) == 2:
        str_counter = "00" + str_counter
    elif len(str_counter) == 3:
        str_counter = "0" + str_counter
    return str_counter


def save_to_csv(filename, lst):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(lst)


def loadImages():
    """
    Initialize a global directory of images.
    This will be called exactly once in the main.
    """
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("../chess/images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))


def drawGameState(screen, board):
    """
    Responsible for all the graphics within current game state.
    """
    drawBoard(screen)  # draw squares on the board
    drawPieces(screen, board)  # draw pieces on top of those squares


def drawBoard(screen):
    """
    Draw the squares on the board.
    The top left square is always light.
    """
    global colors
    colors = [(6, 193, 87), (235, 183, 104)]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(screen, color, p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def drawPieces(screen, board):
    """
    Draw the pieces on the board using the current game_state.board
    """
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def main():
    p.init()
    screen = p.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
    screen.fill(p.Color("white"))
    loadImages()  # do this only once before while loop

    z = 0

    for _ in range(250):
        z = create_board_with_pieces_save_increment_counter(ALL_PIECES, screen, z)
        z = create_board_with_pieces_save_increment_counter(ONLY_PAWNS, screen, z)
        z = create_board_with_pieces_save_increment_counter(ONLY_FIGURES, screen, z)
        z = create_board_with_random_pieces_save_increment_counter(5, screen, z)
        z = create_board_with_random_pieces_save_increment_counter(10, screen, z)
        z = create_board_with_random_pieces_save_increment_counter(15, screen, z)
        z = create_board_with_random_pieces_save_increment_counter(20, screen, z)


if __name__ == "__main__":
    main()
