from rock_paper_scissors.player import Player


def test_create_player():
    player = Player("Tom")
    assert player.name == "Tom"
    assert player.score == 0


def test_change_score():
    player = Player("Tom")
    player.score += 1
    assert player.score == 1
