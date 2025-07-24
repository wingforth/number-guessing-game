import sys


def run():
    from number_guessing_game.number_guessing_game import play_game

    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nCancelled by user.")
        return 1
    except Exception as e:
        print(e)
        return 2


if __name__ == "__main__":
    if not __package__:
        from pathlib import Path

        sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
        import number_guessing_game  # noqa: F401

        sys.path.pop(0)
    sys.exit(run())
