import random
import chess
from engine.evaluate import evaluate

board = chess.Board()

while not board.is_game_over():
    print(board)
    print(f"Оценка: {evaluate(board)}")
    print()

    if board.turn == chess.WHITE:
        move_str = input("Твой ход (например, e2e4): ")
        try:
            move = chess.Move.from_uci(move_str)
        except ValueError:
            print("Неверный формат хода")
            continue
        if move not in board.legal_moves:
            print("Недопустимый ход")
            continue
    else:
        move = random.choice(list(board.legal_moves))
        print(f"Бот сходил: {move}")

    board.push(move)

print(board)
print("Результат:", board.result())
