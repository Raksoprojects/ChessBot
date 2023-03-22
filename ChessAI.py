"""
Handling the AI moves.
"""
import random

piece_score = {"K": 1000, "Q": 9, "R": 5, "B": 3.3, "N": 3.2, "p": 1}

knight_scores = [[0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
                 [0.1, 0.2, 0.4, 0.4, 0.4, 0.4, 0.2, 0.1],
                 [0.15, 0.4, 0.46, 0.46, 0.46, 0.47, 0.4, 0.15],
                 [0.15, 0.4, 0.46, 0.46, 0.46, 0.46, 0.4, 0.15],
                 [0.15, 0.35, 0.4, 0.41, 0.41, 0.4, 0.35, 0.15],
                 [0.15, 0.35, 0.35, 0.36, 0.36, 0.35, 0.35, 0.15],
                 [0.1, 0.2, 0.3, 0.4, 0.4, 0.3, 0.2, 0.1],
                 [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]]

bishop_scores = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                 [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                 [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
                 [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
                 [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                 [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
                 [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                 [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]

rook_scores = [[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
               [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]]

queen_scores = [[0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                [0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]]

pawn_scores = [[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
               [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
               [0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3],
               [0.25, 0.25, 0.3, 0.45, 0.45, 0.3, 0.25, 0.25],
               [0.2, 0.2, 0.2, 0.44, 0.44, 0.2, 0.2, 0.2],
               [0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25],
               [0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25],
               [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]                     

kingEarlyTable = [[-0.3, -0.4, -0.4,-0.5,-0.5,-0.4,-0.4,-0.3],
                [-0.3,-0.4,-0.4,-0.5,-0.5,-0.4,-0.4,-0.3],
                [-0.3,-0.4,-0.4,-0.5,-0.5,-0.4,-0.4,-0.3],
                [-0.3,-0.4,-0.4,-0.5,-0.5,-0.4,-0.4,-0.3],
                [-0.2,-0.3,-0.3,-0.4,-0.4,-0.3,-0.3,-0.2],
                [-0.1,-0.2,-0.2,-0.2,-0.2,-0.2,-0.2,-0.1],
                [0.2, 0.2, 0, 0, 0, 0, 0.2, 0.2],
                [0.2, 0.3, 0.1, 0, 0, 0.1, 0.3, 0.2]]

kingLateTable = [[-0.5,-0.4,-0.3,-0.2,-0.2,-0.3,-0.4,-0.5],
                [-0.3,-0.2,-0.1, 0, 0,-0.1,-0.2,-0.3],
                [-0.3,-0.1, 0.2, 0.3, 0.3, 0.2,-0.1,-0.3],
                [-0.3,-0.1, 0.3, 0.4, 0.4, 0.3,-0.1,-0.3],
                [-0.3,-0.1, 0.3, 0.4, 0.4, 0.3,-0.1,-0.3],
                [-0.3,-0.1, 0.2, 0.3, 0.3, 0.2,-0.1,-0.3],
                [-0.3,-0.3, 0, 0, 0, 0,-0.3,-0.3],
                [-0.5,-0.3,-0.3,-0.3,-0.3,-0.3,-0.3,-0.5]]

piece_position_scores = {"wN": knight_scores,
                         "bN": knight_scores[::-1],
                         "wB": bishop_scores,
                         "bB": bishop_scores[::-1],
                         "wQ": queen_scores,
                         "bQ": queen_scores[::-1],
                         "wR": rook_scores,
                         "bR": rook_scores[::-1],
                         "wp": pawn_scores,
                         "bp": pawn_scores[::-1]}

CHECKMATE = 1000
STALEMATE = 0
DEPTH = 4


def findBestMove(game_state, valid_moves, return_queue, which_algorithm):
    global next_move
    global DEPTH
    next_move = None
    
    if which_algorithm == 2:
        DEPTH = 3
        miniMax(game_state, valid_moves, DEPTH, 1 if game_state.white_to_move else -1, True)
    elif which_algorithm == 3:
        DEPTH = 4 + game_state.moreDepth
        findMoveNegaMaxAlphaBeta(game_state, valid_moves, DEPTH, -CHECKMATE, CHECKMATE,
                              1 if game_state.white_to_move else -1)
    else:
        findRandomMove(valid_moves)
    
    return_queue.put(next_move)


def miniMax(game_state, valid_moves, depth, turn_multiplier, maximazing=True):
    global next_move

    if depth == 0:
        return turn_multiplier * scoreBoard(game_state)

    random.shuffle(valid_moves)
    if maximazing:
        max_score = -CHECKMATE
        for move in valid_moves:
            game_state.makeMove(move)
            next_moves = game_state.getValidMoves()
            score = miniMax(game_state, next_moves, depth-1, turn_multiplier, False)
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
            score = miniMax(game_state, next_moves, depth-1, turn_multiplier, True)
            if score < min_score:
                min_score = score
                if depth == DEPTH:
                    next_move = move
            game_state.undoMove()  
        return min_score    

def findMoveNegaMaxAlphaBeta(game_state, valid_moves, depth, alpha, beta, turn_multiplier):
    global next_move
    if depth == 0:
        return turn_multiplier * scoreBoard(game_state)
    
    random.shuffle(valid_moves)
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
    for row in range(len(game_state.board)):
        for col in range(len(game_state.board[row])):
            piece = game_state.board[row][col]
            if piece != "--":
                piece_position_score = 0
                if piece[1] != "K":
                    piece_position_score = piece_position_scores[piece][row][col]
                else:
                    if game_state.isLateGame:
                        piece_position_score = (kingLateTable[row][col] + 0.5)
                    else:
                        piece_position_score = (kingEarlyTable[row][col] + 0.5)   
                if piece[0] == "w":
                    score += (piece_score[piece[1]] + piece_position_score)
                elif piece[0] == "b":
                    score -= (piece_score[piece[1]] + piece_position_score)

    return score


def findRandomMove(valid_moves):
    """
    Picks and returns a random valid move.
    """
    return random.choice(valid_moves)
