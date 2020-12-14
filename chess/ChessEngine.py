'''
Storing all the information about the current state of chess game.
Determining valid moves at current state.
It will keep move log.
'''

class GameState():
    def __init__(self):
        #Board is an 8x8 2d list, each element in list has 2 characters.
        #The first character represtents the color of the piece: 'b' or 'w'.
        #The second character represtents the type of the piece: 'R', 'N', 'B', 'Q', 'K' or 'p'.
        #"--" represents an empty space with no piece.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []
