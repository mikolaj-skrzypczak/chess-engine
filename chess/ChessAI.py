"""
Handling the AI moves.
"""
import random

piece_score = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}
CHECKMATE = 1000
STALEMATE = 0
DEPTH = 3


# deprecated
def findRandomMove(valid_moves):
    """
    Picks and returns a random valid move.
    """
    return random.choice(valid_moves)


# deprecated
def findBestMove(game_state, valid_moves):
    """
    Greedy algorithm to find the best move based on material alone.
    """
    turn_multiplier = 1 if game_state.white_to_move else -1
    opponent_min_max_score = CHECKMATE
    best_player_move = None
    random.shuffle(valid_moves)
    for player_move in valid_moves:
        game_state.makeMove(player_move)
        if game_state.stalemate:
            opponent_max_score = STALEMATE
        elif game_state.checkmate:
            opponent_max_score = -CHECKMATE
        else:
            opponent_moves = game_state.getValidMoves()
            opponent_max_score = -CHECKMATE
            for opponent_move in opponent_moves:
                game_state.makeMove(opponent_move)
                game_state.getValidMoves()
                if game_state.checkmate:
                    score = CHECKMATE
                elif game_state.stalemate:
                    score = STALEMATE
                else:
                    score = -turn_multiplier * scoreMaterial(game_state.board)
                if score > opponent_max_score:
                    opponent_max_score = score
                game_state.undoMove()
        if opponent_max_score < opponent_min_max_score:
            opponent_min_max_score = opponent_max_score
            best_player_move = player_move
        game_state.undoMove()
    return best_player_move


# deprecated
def findBestMoveMinMax(game_state, valid_moves):
    """
    Helper method to make the first recursive call
    """
    global next_move
    next_move = None
    random.shuffle(valid_moves)
    findMoveMinMax(game_state, valid_moves, DEPTH, game_state.white_to_move)
    return next_move


# deprecated
def findMoveMinMax(game_state, valid_moves, depth, white_to_move):
    global next_move
    if depth == 0:
        return scoreBoard(game_state)
    if white_to_move:
        max_score = -CHECKMATE
        for move in valid_moves:
            game_state.makeMove(move)
            next_moves = game_state.getValidMoves()
            score = findMoveMinMax(game_state, next_moves, depth - 1, False)
            if score > max_score:
                max_score = score
                if depth == DEPTH:
                    next_move = move
            game_state.undoMove()
        return max_score
    else:
        min_score = CHECKMATE
        for move in valid_moves:
            game_state.makeMove(move)
            next_moves = game_state.getValidMoves()
            score = findMoveMinMax(game_state, next_moves, depth - 1, True)
            if score < min_score:
                min_score = score
                if depth == DEPTH:
                    next_move = move
            game_state.undoMove()
        return min_score


# deprecated
def findBestMoveNegaMax(game_state, valid_moves):
    global next_move
    next_move = None
    random.shuffle(valid_moves)
    findMoveNegaMax(game_state, valid_moves, DEPTH, 1 if game_state.white_to_move else -1)
    return next_move


# deprecated
def findMoveNegaMax(game_state, valid_moves, depth, turn_multiplier):
    global next_move
    if depth == 0:
        return turn_multiplier * scoreBoard(game_state)

    max_score = -CHECKMATE
    for move in valid_moves:
        game_state.makeMove(move)
        next_moves = game_state.getValidMoves()
        score = -findMoveNegaMax(game_state, next_moves, depth - 1, -turn_multiplier)
        if score > max_score:
            max_score = score
            if depth == DEPTH:
                next_move = move
        game_state.undoMove()
    return max_score


def findBestMoveNegaMaxAlphaBeta(game_state, valid_moves):
    global next_move
    next_move = None
    random.shuffle(valid_moves)
    findMoveNegaMaxAlphaBeta(game_state, valid_moves, DEPTH, -CHECKMATE, CHECKMATE,
                             1 if game_state.white_to_move else -1)
    return next_move


def findMoveNegaMaxAlphaBeta(game_state, valid_moves, depth, alpha, beta, turn_multiplier):
    global next_move
    if depth == 0:
        return turn_multiplier * scoreBoard(game_state)

    # move ordering - implement later //TODO
    max_score = -CHECKMATE
    for move in valid_moves:
        game_state.makeMove(move)
        next_moves = game_state.getValidMoves()
        score = -findMoveNegaMaxAlphaBeta(game_state, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)
        if score > max_score:
            max_score = score
            if depth == DEPTH:
                next_move = move
        game_state.undoMove()
        if max_score > alpha:
            alpha = max_score
        if alpha >= beta:
            break
    return max_score


def scoreBoard(game_state):
    """
    Score the board. A positive score is good for white, a negative score is good for black.
    """
    if game_state.checkmate:
        if game_state.white_to_move:
            return -CHECKMATE  # black wins
        else:
            return CHECKMATE  # white wins
    elif game_state.stalemate:
        return STALEMATE
    score = 0
    for row in game_state.board:
        for square in row:
            if square[0] == 'w':
                score += piece_score[square[1]]
            elif square[0] == 'b':
                score -= piece_score[square[1]]
    return score


# deprecated
def scoreMaterial(board):
    """
    Score the board based on material.

    """
    score = 0
    for row in board:
        for square in row:
            if square[0] == 'w':
                score += piece_score[square[1]]
            elif square[0] == 'b':
                score -= piece_score[square[1]]
    return score
