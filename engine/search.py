import random
import chess
from engine.evaluate import evaluate, PIECE_VALUES

INF = float("inf")

# счётчик просмотренных позиций, чтобы сравнивать скорость
stats = {"nodes": 0}


def order_moves(board):
    """Сортирует ходы: сначала выгодные взятия и превращения."""

    def move_score(move):
        if board.is_capture(move):
            victim = board.piece_type_at(move.to_square)
            if victim is None:  # взятие на проходе
                victim = chess.PAWN
            attacker = board.piece_type_at(move.from_square)
            # чем ценнее жертва и дешевле атакующий, тем раньше смотрим
            return 10 * PIECE_VALUES[victim] - PIECE_VALUES[attacker]
        if move.promotion:
            return PIECE_VALUES[move.promotion]
        return 0

    return sorted(board.legal_moves, key=move_score, reverse=True)


def minimax(board, depth, maximizing):
    """Обычный minimax без отсечений (для сравнения скорости)."""
    stats["nodes"] += 1
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    if maximizing:
        best = -INF
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, False)
            board.pop()
            best = max(best, score)
        return best
    else:
        best = INF
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, True)
            board.pop()
            best = min(best, score)
        return best


def alphabeta(board, depth, alpha, beta, maximizing):
    """Minimax с alpha-beta отсечением и сортировкой ходов."""
    stats["nodes"] += 1
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    if maximizing:
        best = -INF
        for move in order_moves(board):
            board.push(move)
            score = alphabeta(board, depth - 1, alpha, beta, False)
            board.pop()
            best = max(best, score)
            alpha = max(alpha, best)
            if alpha >= beta:
                break
        return best
    else:
        best = INF
        for move in order_moves(board):
            board.push(move)
            score = alphabeta(board, depth - 1, alpha, beta, True)
            board.pop()
            best = min(best, score)
            beta = min(beta, best)
            if alpha >= beta:
                break
        return best


def find_best_move(board, depth=3, use_alphabeta=True):
    """Выбирает лучший ход для стороны, которая сейчас ходит."""
    maximizing = board.turn == chess.WHITE
    best_score = -INF if maximizing else INF
    best_moves = []

    for move in order_moves(board):
        board.push(move)
        if use_alphabeta:
            score = alphabeta(board, depth - 1, -INF, INF, not maximizing)
        else:
            score = minimax(board, depth - 1, not maximizing)
        board.pop()

        if score == best_score:
            best_moves.append(move)
        elif (maximizing and score > best_score) or (not maximizing and score < best_score):
            best_score = score
            best_moves = [move]

    return random.choice(best_moves)
