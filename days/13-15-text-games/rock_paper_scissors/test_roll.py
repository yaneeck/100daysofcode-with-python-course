import pytest

from rock_paper_scissors.roll import Roll


def test_create_roll():
    roll = Roll()
    assert roll.name in Roll.options()


@pytest.mark.parametrize("choice", Roll.options())
def test_tie(choice):
    roll = Roll(choice)
    assert roll.defeats(choice) is None
