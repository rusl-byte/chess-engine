import chess
from engine.search import find_best_move, config

# Белые: ферзь d1, король e1. Чёрные: король e8, пешки d5 и e6.
# Qxd5 выигрывает пешку, но после exd5 белые теряют ферзя.
board = chess.Board("4k3/8/4p3/3p4/8/8/8/3QK3 w - - 0 1")
bad_move = chess.Move.from_uci("d1d5")

config["quiescence"] = False
move = find_best_move(board, depth=1)
print("Без quiescence:", move)
assert move == bad_move  # бот не видит рекапчура и берёт пешку

config["quiescence"] = True
move = find_best_move(board, depth=1)
print("С quiescence:  ", move)
assert move != bad_move  # бот видит, что ферзя съедят

print("Проверки пройдены")
