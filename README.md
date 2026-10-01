# Chess Engine

A chess engine written in Python. The goal of the project is to build the "brain" of a chess program step by step: from a random-move bot to a search-based engine using minimax and alpha-beta pruning.

Move legality and board state are handled by the [`python-chess`](https://python-chess.readthedocs.io/) library. The evaluation and search logic is written from scratch.

## Status

Work in progress. Current stage: **console game against a random bot**.

## Roadmap

- [x] Console game: play White against a bot that picks random legal moves
- [ ] Position evaluation (material count)
- [ ] Minimax search
- [ ] Alpha-beta pruning
- [ ] Piece-square tables and move ordering
- [ ] Iterative deepening with a time limit
- [ ] Quiescence search and transposition table
- [ ] UCI protocol support (play from a GUI or on Lichess)

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

## Tech stack

- Python 3
- [python-chess](https://pypi.org/project/chess/)

## Learning resources

- [Chess Programming Wiki](https://www.chessprogramming.org/)
- [python-chess documentation](https://python-chess.readthedocs.io/)
