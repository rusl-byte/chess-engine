import chess
from engine.search import find_best_move

# У белых под боем висит ферзь на d4, чёрные ходят.
# Пешка e5 может его съесть.
board = chess.Board("4k3/8/8/4p3/3Q4/8/8/4K3 b - - 0 1")
print(board)
print("Лучший ход:", find_best_move(board, depth=2))  # ожидаем e5d4
