import argparse
import os
import random
import shutil
import sys

import chess
import chess.engine
import chess.pgn

MAX_PLIES = 300  # если партия не кончилась, считаем ничьей


def play_game(ours, stockfish, our_color, our_limit, sf_limit, random_plies):
    board = chess.Board()
    # несколько случайных ходов в начале, чтобы партии не были одинаковыми
    for _ in range(random_plies):
        board.push(random.choice(list(board.legal_moves)))

    while not board.is_game_over(claim_draw=True) and board.ply() < MAX_PLIES:
        if board.turn == our_color:
            result = ours.play(board, our_limit)
        else:
            result = stockfish.play(board, sf_limit)
        board.push(result.move)

    if board.is_game_over(claim_draw=True):
        outcome = board.result(claim_draw=True)
    else:
        outcome = "1/2-1/2"
    return board, outcome


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--games", type=int, default=2)
    parser.add_argument("--elo", type=int, default=1320)
    parser.add_argument("--depth", type=int, default=3)
    parser.add_argument("--random-plies", type=int, default=2)
    parser.add_argument("--stockfish", default=None)
    parser.add_argument("--pgn", default="results.pgn")
    args = parser.parse_args()

    sf_path = args.stockfish or shutil.which("stockfish") or "/usr/games/stockfish"
    here = os.path.dirname(os.path.abspath(__file__))
    our_cmd = [sys.executable, os.path.join(here, "uci.py")]

    wins = draws = losses = 0

    with chess.engine.SimpleEngine.popen_uci(our_cmd) as ours, \
            chess.engine.SimpleEngine.popen_uci(sf_path) as sf:

        opt = sf.options["UCI_Elo"]
        elo = max(opt.min, min(opt.max, args.elo))
        sf.configure({"UCI_LimitStrength": True, "UCI_Elo": elo})
        print(f"Stockfish: UCI_Elo = {elo}, наш бот: глубина {args.depth}")

        our_limit = chess.engine.Limit(depth=args.depth)
        sf_limit = chess.engine.Limit(time=0.1)

        for i in range(args.games):
            our_color = chess.WHITE if i % 2 == 0 else chess.BLACK
            board, outcome = play_game(
                ours, sf, our_color, our_limit, sf_limit, args.random_plies
            )

            if outcome == "1/2-1/2":
                draws += 1
                text = "ничья"
            elif (outcome == "1-0") == (our_color == chess.WHITE):
                wins += 1
                text = "победа"
            else:
                losses += 1
                text = "поражение"

            color_name = "белые" if our_color == chess.WHITE else "чёрные"
            print(f"Партия {i + 1}/{args.games}: {color_name}, {outcome}, {text}")

            game = chess.pgn.Game.from_board(board)
            ours_name, sf_name = "PyChessEngine", f"Stockfish {elo}"
            game.headers["White"] = ours_name if our_color == chess.WHITE else sf_name
            game.headers["Black"] = sf_name if our_color == chess.WHITE else ours_name
            game.headers["Result"] = outcome
            with open(args.pgn, "a") as f:
                print(game, file=f, end="\n\n")

    total = wins + draws + losses
    score = (wins + 0.5 * draws) / total
    print()
    print(f"Итог: {wins} побед, {draws} ничьих, {losses} поражений из {total}")
    print(f"Очки: {wins + 0.5 * draws} из {total} ({score:.0%})")


if __name__ == "__main__":
    main()

