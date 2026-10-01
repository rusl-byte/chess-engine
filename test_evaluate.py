import chess
from engine.evaluate import evaluate

# Начальная позиция: поровну
assert evaluate(chess.Board()) == 0

# У чёрных нет ферзя: белые сильно впереди
board = chess.Board("rnb1kbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
print("Чёрные без ферзя:", evaluate(board))
assert 800 < evaluate(board) < 1000

# У белых нет ладьи: чёрные впереди
board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/1NBQKBNR w Kkq - 0 1")
print("Белые без ладьи:", evaluate(board))
assert -600 < evaluate(board) < -400

# Конь в центре лучше, чем в углу
center = chess.Board("4k3/8/8/8/3N4/8/P7/4K3 w - - 0 1")
corner = chess.Board("4k3/8/8/8/8/8/P7/N3K3 w - - 0 1")
print("Конь в центре:", evaluate(center), "| конь в углу:", evaluate(corner))
assert evaluate(center) > evaluate(corner)

# Мат чёрными
board = chess.Board()
for move in ["f3", "e5", "g4", "Qh4"]:
    board.push_san(move)
assert evaluate(board) == -100000

print("Все проверки пройдены")
