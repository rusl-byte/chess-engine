import time
import chess
from engine.search import minimax, alphabeta, stats, INF

# Середина партии (итальянская партия, после 3 ходов)
board = chess.Board("r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3")
DEPTH = 3

stats["nodes"] = 0
start = time.time()
score1 = minimax(board, DEPTH, True)
t1 = time.time() - start
n1 = stats["nodes"]

stats["nodes"] = 0
start = time.time()
score2 = alphabeta(board, DEPTH, -INF, INF, True)
t2 = time.time() - start
n2 = stats["nodes"]

print(f"Minimax:    оценка {score1}, позиций {n1}, время {t1:.2f} с")
print(f"Alpha-beta: оценка {score2}, позиций {n2}, время {t2:.2f} с")
print(f"Ускорение: в {n1 / n2:.1f} раз по числу позиций")
print("Оценки совпали:", score1 == score2)

# Alpha-beta на большей глубине
DEPTH = 4
stats["nodes"] = 0
start = time.time()
alphabeta(board, DEPTH, -INF, INF, True)
print(f"Alpha-beta, глубина {DEPTH}: позиций {stats['nodes']}, время {time.time() - start:.2f} с")
