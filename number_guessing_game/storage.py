import json
from collections import deque
from pathlib import Path
from number_guessing_game.config import DIFFICULTY


class TopScoreList:
    def __init__(self, max_length: int, score_file: Path) -> None:
        """_summary_

        Args:
            max_length (int): _description_
            score_file (Path): _description_
        """
        self._ensure_dir_exist(score_file.parent)
        # Number of high scores that are stored for every difficulty level.
        self.max_length = max_length
        # File that stores scores.
        self.score_file: Path = score_file
        self.__scores: dict[str, deque[tuple[int, float, str]]] = {}
        self.__updated: bool = False

    @staticmethod
    def _ensure_dir_exist(directory: Path) -> None:
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
            return
        if not directory.is_dir():
            raise NotADirectoryError(f"{directory} is not a directory.")

    def load_scores(self) -> None:
        if not self.score_file.exists():
            self.__scores = {level: deque(maxlen=self.max_length) for level, _ in DIFFICULTY}
        if self.score_file.is_dir():
            raise IsADirectoryError(f"{self.score_file} is not a file.")
        with open(self.score_file, mode="r", encoding="utf-8") as fd:
            try:
                data = json.load(fd)
            except json.JSONDecodeError:
                self.__scores = {level: deque(maxlen=self.max_length) for level, _ in DIFFICULTY}
                return
        self.__scores = {level: deque(map(tuple, records), maxlen=self.max_length) for level, records in data.items()}

    def save_scores(self) -> None:
        data = {level: list(records) for level, records in self.__scores.items()}
        with open(self.score_file, mode="w", encoding="utf-8") as fd:
            return json.dump(data, fd, indent=4)

    def ranking(self, score: tuple[int, float], difficulty_level: str) -> int | None:
        high_scores = self.__scores[difficulty_level]
        if len(high_scores) == self.max_length and score >= high_scores[-1][:2]:
            return None
        for ranking, (attempts, time_taken, _) in enumerate(high_scores, 1):
            if score < (attempts, time_taken):
                return ranking
        else:
            return len(high_scores) + 1

    def get_top_score_list(self, difficulty_level: str) -> deque[tuple[int, float, str]]:
        return self.__scores[difficulty_level]

    def clear(self) -> None:
        for scores in self.__scores.values():
            scores.clear()
        self.save_scores()

    def update_scores(self, ranking: int, score: tuple[int, float], player: str, difficulty_level: str):
        self.__scores[difficulty_level].insert(ranking - 1, (*score, player))
        self.__updated = True

    def __enter__(self):
        self.load_scores()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.__updated:
            self.save_scores()
