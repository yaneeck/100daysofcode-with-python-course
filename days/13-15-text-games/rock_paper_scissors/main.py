from player import Player
from roll import Roll


def print_header():
    print("--- Rock - Paper - Scissors ---")


def get_players_name():
    return input("What is your name? ")


def game_loop(player1, player2, rolls: int = 3) -> None:
    for _ in range(rolls):
        p1_roll = Roll(input("Choose a roll: paper, rock, or scissors "))
        p2_roll = Roll()

        outcome = p1_roll.defeats(p2_roll.name)

        # display throws
        print(f"{player1.name} throws: {p1_roll.name}")
        print(f"{player2.name} throws: {p2_roll.name}")

        # display winner for this round
        if outcome:
            print(f"{player1.name} wins!")
            player1.score += 1
        elif outcome is None:
            print("It's a tie!")
        else:
            print(f"{player2.name} wins!")
            player2.score += 1  # added score update when player wins

    # Compute who won
    if player1.score > player2.score:
        print(f"{player1.name} wins the game!")
    elif player1.score < player2.score:
        print(f"{player2.name} wins the game!")
    else:
        print("The game is a tie!")


def build_the_three_rolls() -> list[Roll]:
    return [Roll() for _ in range(3)]


def main():
    print_header()

    player1 = Player(get_players_name())
    player2 = Player("computer")

    game_loop(player1, player2)


if __name__ == "__main__":
    main()
