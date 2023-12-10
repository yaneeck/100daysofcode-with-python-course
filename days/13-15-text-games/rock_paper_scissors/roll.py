import random


class Roll:

    def __init__(self, choice: str | None = None):
        if choice:
            self._name = choice
        else:
            self._name = Roll.options()[random.randint(0, 2)]

    @property
    def name(self) -> str:
        return self._name

    @staticmethod
    def options() -> list:
        return ["rock", "paper", "scissors"]

    @staticmethod
    def rules() -> dict:
        return {
            "rock": {"defeats": "scissors", "defeated by": "paper"},
            "paper": {"defeats": "rock", "defeated by": "scissors"},
            "scissors": {"defeats": "rock", "defeated by": "rock"}
        }

    def defeats(self, choice: str) -> bool:
        return Roll.rules()[self._name]["defeats"] == choice
