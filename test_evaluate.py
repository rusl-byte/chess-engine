import chess
from engine.evaluate import evaluate

# Начальная позиция: поровну
board = chess.Board()
print("Начальная позиция:", evaluate(board))  # ожидаем 0

# У чёрных нет ферзя
board = chess.Board("rnb1kbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
print("Чёрные без ферзя:", evaluate(board))  # ожидаем 900

# У белых нет ладьи
board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/1NBQKBNR w Kkq - 0 1")
print("Белые без ладьи:", evaluate(board))  # ожидаем -500

# Детский мат: чёрные побеждают
board = chess.Board()
for move in ["f3", "e5", "g4", "Qh4"]:
    board.push_san(move)
print("Мат чёрными:", evaluate(board))  # ожидаем -100000
