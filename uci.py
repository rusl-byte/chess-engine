import sys
import chess
from engine.search import find_best_move

DEFAULT_DEPTH = 3


def send(text):
    print(text, flush=True)


def parse_position(tokens):
    """Разбирает: position startpos|fen <...> [moves e2e4 e7e5 ...]"""
    if "moves" in tokens:
        i = tokens.index("moves")
        head, moves = tokens[:i], tokens[i + 1:]
    else:
        head, moves = tokens, []

    if head and head[0] == "fen":
        board = chess.Board(" ".join(head[1:]))
    else:
        board = chess.Board()

    for move in moves:
        board.push_uci(move)
    return board


def main():
    board = chess.Board()
    depth = DEFAULT_DEPTH

    for line in sys.stdin:
        tokens = line.split()
        if not tokens:
            continue
        cmd = tokens[0]

        if cmd == "uci":
            send("id name PyChessEngine")
            send("id author rusl-byte")
            send(f"option name Depth type spin default {DEFAULT_DEPTH} min 1 max 6")
            send("uciok")
        elif cmd == "isready":
            send("readyok")
        elif cmd == "ucinewgame":
            board = chess.Board()
        elif cmd == "setoption":
            if "name" in tokens and "value" in tokens:
                n, v = tokens.index("name"), tokens.index("value")
                name = " ".join(tokens[n + 1:v]).lower()
                if name == "depth":
                    depth = int(tokens[v + 1])
        elif cmd == "position":
            board = parse_position(tokens[1:])
        elif cmd == "go":
            search_depth = depth
            if "depth" in tokens:
                search_depth = int(tokens[tokens.index("depth") + 1])
            if board.is_game_over():
                send("bestmove 0000")
            else:
                move = find_best_move(board, search_depth)
                send(f"bestmove {move.uci()}")
        elif cmd == "quit":
            break


if __name__ == "__main__":
    main()
