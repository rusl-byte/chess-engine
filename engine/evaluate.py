import chess

PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 300,
    chess.BISHOP: 300,
    chess.ROOK: 500,
    chess.QUEEN: 900,
}

MATE_SCORE = 100000


def evaluate(board):
    """Оценка позиции: > 0 лучше белые, < 0 лучше чёрные."""
    if board.is_checkmate():
        # Если мат, то проиграл тот, чей сейчас ход
        return -MATE_SCORE if board.turn == chess.WHITE else MATE_SCORE

    if board.is_game_over():
        return 0  # пат или ничья

    score = 0
    for piece_type, value in PIECE_VALUES.items():
        score += len(board.pieces(piece_type, chess.WHITE)) * value
        score -= len(board.pieces(piece_type, chess.BLACK)) * value
    return score
