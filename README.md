# Chess Engine

A chess engine written in Python. The goal of the project is to build the "brain" of a chess program step by step: from a random-move bot to a search-based engine using minimax and alpha-beta pruning.

Move legality and board state are handled by the [`python-chess`](https://python-chess.readthedocs.io/) library. The evaluation and search logic is written from scratch.

## Status

Alpha-beta search with piece-square evaluation, quiescence search and UCI support.

## Roadmap

- [x] Console game: play against the engine as White or Black
- [x] Position evaluation (material count)
- [x] Minimax search
- [x] Alpha-beta pruning
- [x] Piece-square tables and move ordering
- [x] Quiescence search
- [x] UCI protocol support
- [ ] Iterative deepening with a time limit
- [ ] Transposition table

## Getting started

Requires Python 3.8+.

```bash
git clone https://github.com/rusl-byte/chess-engine.git
cd chess-engine

python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python main.py
```

## How to play

You play White. Enter moves in UCI notation: the starting square followed by the target square.

```
Your move (e.g. e2e4): e2e4
```

| Move | Notation |
|------|----------|
| Pawn e2 to e4 | `e2e4` |
| Knight g1 to f3 | `g1f3` |
| Pawn e7 to e8, promote to queen | `e7e8q` |

The game ends on checkmate, stalemate, or a draw, and prints the result (`1-0`, `0-1` or `1/2-1/2`).
Press `Ctrl+C` to quit.

## How it works

The engine will consist of two parts:

1. **Evaluation**: a function that scores a position. Positive means White is better. The first version counts material (pawn = 1, knight/bishop = 3, rook = 5, queen = 9).
2. **Search**: looks several moves ahead, assuming both sides play their best (minimax), and skips branches that cannot change the result (alpha-beta pruning).

## Project structure

```
chess-engine/
├── main.py            # console game loop
├── requirements.txt   # dependencies
└── README.md
```

The `engine/` package with `evaluate.py` and `search.py` will be added in the next stages.

## Benchmarks

Test position: Italian Game after 3 moves, search depth 3.

| Search | Positions searched | Time |
|--------|-------------------:|-----:|
| Minimax | 24,942 | 1.08 s |
| Alpha-beta + move ordering | 1,262 | 0.06 s |

Alpha-beta with move ordering searches about **20x fewer positions** and returns the same evaluation.
Reproduce: `python test_speed.py`

## Match against Stockfish

20 games, colors alternated, first 2 plies random for variety.
Engine: depth 3. Opponent: Stockfish with `UCI_LimitStrength` on and `UCI_Elo = 1320`, 0.1 s per move.

| Wins | Draws | Losses | Score |
|-----:|------:|-------:|------:|
| 13 | 2 | 5 | 14 / 20 (70%) |

Twenty games give a wide margin of error (about 51-89% at 95% confidence), and Stockfish's
`UCI_Elo` is calibrated for different time controls, so this is a rough indicator, not an exact rating.
Games are saved in `results.pgn`.

Reproduce: `python match.py --games 20 --elo 1320 --depth 3`

## UCI

The engine speaks the UCI protocol, so it can be plugged into GUIs such as Cute Chess or Arena:

    python /path/to/chess-engine-repo/uci.py
## Tech stack

- Python 3
- [python-chess](https://pypi.org/project/chess/)

## Learning resources

- [Chess Programming Wiki](https://www.chessprogramming.org/)
- [python-chess documentation](https://python-chess.readthedocs.io/)
