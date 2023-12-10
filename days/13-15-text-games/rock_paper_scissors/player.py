class Player:

    def __init__(self, name: str):
        self._name = name
        self._score = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int):
        self._score = value
