import random
from typing import Union


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
            "scissors": {"defeats": "paper", "defeated by": "rock"}
        }

    def defeats(self, choice: str) -> Union[bool, None]:
        if self._name == choice:
            return None
        return Roll.rules()[self._name]["defeats"] == choice

