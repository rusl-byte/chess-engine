import chess
from engine.evaluate import evaluate
from engine.search import find_best_move

DEPTH = 3


def choose_color():
    while True:
        answer = input("За кого играешь? (1 - белые, 2 - чёрные): ").strip()
        if answer == "1":
            return chess.WHITE
        if answer == "2":
            return chess.BLACK
        print("Введи 1 или 2")


def show_board(board, player_color):
    """Печатает доску с координатами, фигуры игрока внизу."""
    rows = str(board).split("\n")
    ranks = list(range(8, 0, -1))
    files = list("abcdefgh")
    if player_color == chess.BLACK:
        rows = [" ".join(reversed(r.split(" "))) for r in reversed(rows)]
        ranks.reverse()
        files.reverse()
    for rank, row in zip(ranks, rows):
        print(f"{rank}  {row}")
    print()
    print("   " + " ".join(files))


player_color = choose_color()
board = chess.Board()
first_prompt = True  # пример хода показываем только до первого хода игрока

while not board.is_game_over():
    show_board(board, player_color)
    print(f"Оценка: {evaluate(board)}")
    print()

    if board.turn == player_color:
        example = "e2e4" if player_color == chess.WHITE else "e7e5"
        prompt = f"Твой ход (например, {example}): " if first_prompt else "Твой ход: "
        move_str = input(prompt)
        try:
            move = chess.Move.from_uci(move_str)
        except ValueError:
            print("Неверный формат хода")
            continue
        if move not in board.legal_moves:
            print("Недопустимый ход")
            continue
        first_prompt = False
    else:
        print("Бот думает...")
        move = find_best_move(board, DEPTH)
        print(f"Бот сходил: {move}")

    board.push(move)

show_board(board, player_color)
print("Результат:", board.result())
