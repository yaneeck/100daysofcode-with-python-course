import random
from typing import Union


class Roll:

    def __init__(self, choice: str | None = None):
        if choice:
            self._name = choice
        else:
            self._name = Roll.options()[random.randint(0, 14)]

    @property
    def name(self) -> str:
        return self._name

    @staticmethod
    def options() -> list:
        return [
            "rock", "gun", "lightning",
            "devil", "dragon", "water",
            "air", "paper", "sponge",
            "wolf", "tree", "human",
            "snake", "scissors", "fire"
        ]

    @staticmethod
    def wins() -> dict:
        return {
            "rock": ["sponge", "wolf", "tree", "human", "snake" "scissors", "fire"],
            "gun": ["rock", "wolf", "tree", "human", "snake", "scissors", "fire"],
            "lightning": ["rock", "gun", "tree", "human", "snake", "scissors", "fire"],
            "devil": ["rock", "gun", "lightning", "human", "snake", "scissors", "fire"],
            "dragon": ["rock", "gun", "lightning", "snake", "scissors", "fire"],
            "water": ["rock", "gun", "lightning", "devil", "dragon", "scissors", "fire"],
            "air": ["rock", "gun", "lightning", "devil", "dragon", "water", "fire"],
            "paper": ["rock", "gun", "lightning", "devil", "dragon", "water", "air"],
            "sponge": ["gun", "lightning", "devil", "dragon", "water", "air", "paper"],
            "wolf": ["lightning", "devil", "dragon", "water", "air", "paper", "sponge"],
            "tree": ["devil", "dragon", "water", "air", "paper", "sponge", "wolf"],
            "human": ["dragon", "water", "air", "paper", "sponge", "wolf", "tree"],
            "snake": ["water", "air", "paper", "sponge", "wolf", "tree", "human"],
            "scissors": ["air", "paper", "sponge", "wolf", "tree", "human", "snake"],
            "fire": ["paper", "sponge", "wolf", "tree", "human", "snake", "scissors"]
        }

    def defeats(self, choice: str) -> Union[bool, None]:
        if self._name == choice:
            return None
        return choice in Roll.wins()[self._name]
