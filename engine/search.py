import random
import chess
from engine.evaluate import evaluate

INF = float("inf")


def minimax(board, depth, maximizing):
    """Возвращает оценку позиции, просчитав depth полуходов вперёд."""
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    if maximizing:  # ходят белые: ищем максимум
        best = -INF
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, False)
            board.pop()
            best = max(best, score)
        return best
    else:  # ходят чёрные: ищем минимум
        best = INF
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, True)
            board.pop()
            best = min(best, score)
        return best


def find_best_move(board, depth=3):
    """Выбирает лучший ход для стороны, которая сейчас ходит."""
    maximizing = board.turn == chess.WHITE
    best_score = -INF if maximizing else INF
    best_moves = []

    for move in board.legal_moves:
        board.push(move)
        score = minimax(board, depth - 1, not maximizing)
        board.pop()

        if score == best_score:
            best_moves.append(move)
        elif (maximizing and score > best_score) or (not maximizing and score < best_score):
            best_score = score
            best_moves = [move]

    return random.choice(best_moves)
