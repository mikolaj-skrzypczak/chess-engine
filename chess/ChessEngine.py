'''
Storing all the information about the current state of chess game.
Determining valid moves at current state.
It will keep move log.
'''

class GameState():
    def __init__(self):
        '''
        Board is an 8x8 2d list, each element in list has 2 characters.
        The first character represtents the color of the piece: 'b' or 'w'.
        The second character represtents the type of the piece: 'R', 'N', 'B', 'Q', 'K' or 'p'.
        "--" represents an empty space with no piece.
        '''
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "wB", "--", "--", "--", "--"],
            ["--", "--", "bB", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.moveFunctions = {"p": self.getPawnMoves, "R": self.getRookMoves, "N": self.getKnightMoves,
                              "B": self.getBishopMoves, "Q": self.getQueenMoves, "K": self.getKingMoves}
        self.white_to_move = True
        self.move_log = []
        

    def makeMove(self, move):
        '''
        Takes a Move as a parameter and exectutes it.
        (this will not work for castling, pawn promotion and en-passant)
        '''
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move) #log the move so we can undo it later
        self.white_to_move = not self.white_to_move #switch players
       
 
    def undoMove(self):
        '''
        Undo the last move
        '''   
        if len(self.move_log) != 0: #make sure that there is a move to undo
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.white_to_move = not self.white_to_move #swap players
            

    def getValidMoves(self):
        '''
        All moves considering checks.
        '''
        return self.getAllPossibleMoves() #for now we will not worry about checks
        
    
    def getAllPossibleMoves(self):
        '''
        All moves without considering checks.
        '''
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                turn = self.board[row][col][0]
                if (turn == "w" and self.white_to_move) or (turn == "b" and not self.white_to_move):
                    piece = self.board[row][col][1]
                    self.moveFunctions[piece](row, col, moves) #calls appropriate move function based on piece type
        return moves
       
             
    def getPawnMoves(self, row, col, moves):
        '''
        Get all the pawn moves for the pawn located at row, col and add the moves to the list.
        '''
        if self.white_to_move: #white pawn moves
            if self.board[row-1][col] == "--": #1 square pawn advance
                moves.append(Move((row, col), (row-1, col), self.board)) #(start square, end square, board)
                if row == 6 and self.board[row-2][col] == "--": #2 square pawn advance
                    moves.append(Move((row, col), (row-2, col), self.board))
            if col - 1 >= 0: #capturing to the left - impossible if a pawn is standing in a far left column
                if self.board[row-1][col-1][0] == "b": #enemy piece to capture
                    moves.append(Move((row, col), (row-1, col-1), self.board))
            if col + 1 <= 7: #capturing to the right - analogical
                if self.board[row-1][col+1][0] == "b": #enemy piece to capture
                    moves.append(Move((row, col), (row-1, col+1), self.board))
        if not self.white_to_move: #black pawn moves
            if self.board[row+1][col] == "--": #1 suare pawn advance
                moves.append(Move((row, col), (row+1, col), self.board))
                if row == 1 and self.board[row+2][col] == "--":
                    moves.append(Move((row ,col), (row+2, col), self.board))
            if col - 1 >= 0:
                if self.board[row+1][col-1][0] == "w":
                    moves.append(Move((row, col), (row+1, col-1), self.board))
            if col + 1 <= 7:
                if self.board[row+1][col+1][0] == "w":
                    moves.append(Move((row, col), (row+1, col+1), self.board))
    
    
    def getRookMoves(self, row, col, moves):
        '''
        Get all the rook moves for the rook located at row, col and add the moves to the list.
        '''
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1)) #up, left, down, right
        enemy_color = "b" if self.white_to_move else "w"
        for direction in directions:
            for i in range(1, 8):
                end_row = row + direction[0] * i
                end_col = col + direction[1] * i
                if 0 <= end_row <= 7 and 0 <= end_col <= 7: #check for possible moves only in boundries of the board
                    end_piece = self.board[end_row][end_col]
                    if end_piece == "--": #empty space is valid
                        moves.append(Move((row, col), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_color: #capture enemy piece
                        moves.append(Move((row, col), (end_row, end_col), self.board))
                        break
                    else: #friendly piece
                        break
                else: #off board
                    break
                        
                        
    def getKnightMoves(self, row, col, moves):
        '''
        Get all the knight moves for the knight located at row col and add the moves to the list.
        '''
        knight_moves = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)) #up/left up/right right/up right/down down/left down/right left/up left/down
        ally_color = "w" if self.white_to_move else "b"
        for move in knight_moves:
            end_row = row + move[0]
            end_col = col + move[1]
            if 0 <= end_row <= 7 and 0 <= end_col <= 7:
                end_piece = self.board[end_row][end_col]
                if end_piece[0] != ally_color: #so it's either enemy piece or empty equare 
                    moves.append(Move((row, col), (end_row, end_col), self.board))
                    
    
    def getBishopMoves(self, row, col, moves):
        '''
        Get all the bishop moves for the bishop located at row col and add the moves to the list.
        '''
        directions = ((-1, -1), (-1, 1), (1, 1), (1, -1)) #digaonals: up/left up/right down/right down/left
        enemy_color = "b" if self.white_to_move else "w"    
        for direction in directions:
            for i in range(1, 8):
                end_row = row + direction[0] * i
                end_col = col + direction[1] * i
                if 0 <= end_row <= 7 and 0 <= end_col <=7: #check if the move is on board
                    end_piece = self.board[end_row][end_col]
                    if end_piece == "--": #empty space is valid
                        moves.append(Move((row, col), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_color: #capture enemy piece
                        moves.append(Move((row, col), (end_row, end_col), self.board))
                        break
                    else: #friendly piece
                        break
                else: #off board
                    break
                    
                


    def getQueenMoves(self, row, col, moves):
        '''
        Get all the queen moves for the queen located at row col and add the moves to the list.
        '''
        pass
    
    
    def getKingMoves(self, row, col, moves):
        '''
        Get all the king moves for the king located at row col and add the moves to the list.
        '''
        pass
    
    
    
        
class Move():
    '''
    in chess fields on the board are described by two symbols, one of them being number between 1-8 (which is corespodning to rows)
    and the second one being a letter between a-f (coresponding to columns), in order to use this notation we need to map our [row][col] coordinates
    to match the ones used in the original chess game
    '''
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4,
                     "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3,
                     "e": 4, "f": 5, "g": 6, "h": 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    
    def __init__(self, start_square, end_square, board):
        self.start_row = start_square[0]
        self.start_col = start_square[1]
        self.end_row = end_square[0]
        self.end_col = end_square[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
        self.moveID = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col 

    
    def __eq__(self, other):
        '''
        Overriding the equals method.
        '''
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False
            
        
    def getChessNotation(self):
        return self.piece_moved + " " + self.getRankFile(self.start_row, self.start_col) + "->" + self.getRankFile(self.end_row, self.end_col) + " " + self.piece_captured 
    
    
    def getRankFile(self, row, col):
        return self.cols_to_files[col] + self.rows_to_ranks[row]
        
        
        
        
        
        