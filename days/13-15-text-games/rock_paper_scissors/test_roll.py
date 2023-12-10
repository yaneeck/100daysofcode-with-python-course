from rock_paper_scissors.roll import Roll


def test_create_roll():
    roll = Roll()
    assert roll.name in ["rock", "paper", "scissors"]


