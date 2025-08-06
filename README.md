# number-guessing-game

🎲 **Number Guessing Game**

A simple and fun number guessing game with multiple difficulty levels and a leaderboard.

## Features
- Three difficulty levels: Easy, Medium, Hard
- Automatic leaderboard recording
- Hint system to help players
- Pure Python implementation, easy to extend

## Installation
Recommended: Python 3.13 or newer. This project uses [uv](https://github.com/astral-sh/uv) for environment and dependency management.

```bash
git clone https://github.com/wingforth/number-guessing-game.git
cd number-guessing-game
uv sync
```

## Run the Game

```bash
uv run number_guessing_game
```

## Run Tests

```bash
uv add --dev pytest pytest-cov
uv run pytest
```

## Project Structure

```
number_guessing_game/
    config.py              # Configuration
    number_guessing_game.py# Game logic
    storage.py             # Leaderboard storage
    __main__.py            # Entry point
data/
    scores.json            # Leaderboard data
tests/
    test_number_guessing_game.py  # Game logic tests
    test_storage.py        # Leaderboard tests
```

## License
MIT
