from re import match
from random import shuffle
from os import system

from pyfiglet import print_figlet  # type: ignore
from rich.console import Console
from rich.markdown import Markdown

from card import Card, RANKS, SUITS
from pile import Stockpile, FoundationPile, Column, move_card
from game import MoveCounter, Timer


def clear_screen() -> None:
    system("cls || clear")


def main() -> None:
    console = Console()

    foundation_piles: list[FoundationPile] = [FoundationPile() for _ in range(4)]
    columns: list[Column] = [Column() for _ in range(7)]

    deck = [Card(rank, suit) for rank in RANKS for suit in SUITS]
    shuffle(deck)

    # Moves cards to columns
    for cards_per_column, column in enumerate(columns, start=1):
        for _ in range(cards_per_column):
            move_card(deck, column.cards)

    # The remaining cards are moved to the stockpile
    stockpile = Stockpile(deck)

    move_counter = MoveCounter()

    timer = Timer()
    timer.start()

    while True:
        clear_screen()

        # Checks if all columns are empty
        if all(not column.cards for column in columns):
            print_figlet("You won!", font="smslant")
            print(
                f"Moves: {move_counter.moves}",
                f"Time: {timer.stop()}",
                sep="\n",
                end="\n\n",
            )
            input("Press 'Enter' to quit...")
            clear_screen()
            break

        # Printing
        print("   S    |  A   B   C   D  | Moves: |")

        print(stockpile.display(), end=" | ")  # Stockpile
        for foundation_pile in foundation_piles:  # Foundation piles
            print(foundation_pile.display(), end=" ")
        print(move_counter.display())

        print("-" * 36)

        for column_index, column in enumerate(columns):  # Columns
            print(column_index, column.display())

        # User command
        command = input("> ")

        if command == "q":
            clear_screen()
            break

        # Moving cards between columns
        elif match(r"^[0-6] [0-6]$", command):
            initial_column_index, target_column_index = map(int, command.split())

            initial_column = columns[initial_column_index]
            target_column = columns[target_column_index]

            for trans_card_index, trans_card in enumerate(initial_column.cards):
                if not trans_card.face_down and trans_card.can_move_to_column(
                    target_column.cards
                ):
                    initial_column.move_cards(target_column.cards, trans_card_index)
                    move_counter.moves += 1
                    break
            else:
                input("Cannot move the selected cards between columns...")

        elif match(r"^[0-6] [a-dA-D]$", command):
            a, b = command.split()
            converter = {"a": 0, "b": 1, "c": 2, "d": 3, "A": 0, "B": 1, "C": 2, "D": 3}

            initial_pile = columns[int(a)].cards
            target_pile = foundation_piles[converter[b]].cards

            if initial_pile:
                trans_card = initial_pile[-1]

                if target_pile:
                    if (
                        RANKS.index(trans_card.rank)
                        == RANKS.index(target_pile[-1].rank) + 1
                        and trans_card.suit == target_pile[-1].suit
                    ):
                        move_card(initial_pile, target_pile)
                        move_counter.moves += 1
                    else:
                        input("Cannot move the selected card to the foundation pile...")
                else:
                    if trans_card.rank == "A":
                        move_card(initial_pile, target_pile)
                        move_counter.moves += 1
                    else:
                        input("You can only move an Ace to an empty foundation pile...")
            else:
                input(f"Column {a.upper()} is empty...")

        elif match(r"^[a-dA-D] [0-6]$", command):
            a, b = command.split()
            converter = {"a": 0, "b": 1, "c": 2, "d": 3, "A": 0, "B": 1, "C": 2, "D": 3}

            initial_pile = foundation_piles[converter[a]].cards
            target_pile = columns[int(b)].cards

            if initial_pile and target_pile[-1].can_move_to_column(target_pile):
                move_card(initial_pile, target_pile)
                move_counter.moves += 1
            else:
                input("Cannot move the selected card to the specified column...")

        elif match(r"^s$", command):
            if stockpile.face_down_cards:
                move_card(stockpile.face_down_cards, stockpile.face_up_cards)
                move_counter.moves += 1
            else:
                # Moves cards from the face-up pile back to the face-down pile
                stockpile.face_up_cards.reverse()  # Restores the order
                stockpile.face_down_cards = stockpile.face_up_cards.copy()
                stockpile.face_up_cards.clear()

        elif match(r"^s [0-6]$", command):
            initial_pile = stockpile.face_up_cards
            if initial_pile:
                trans_card = initial_pile[-1]

                target_column_index = int(command.split()[-1])
                target_column = columns[target_column_index]

                if trans_card.can_move_to_column(target_column.cards):
                    move_card(initial_pile, target_column.cards)
                    move_counter.moves += 1
                else:
                    input(
                        f"Cannot move the card {trans_card} to the specified column..."
                    )
            else:
                input("No cards have been drawn from the stockpile...")

        elif match(r"^s [a-dA-D]$", command):
            initial_pile = stockpile.face_up_cards
            if initial_pile:
                trans_card = initial_pile[-1]

                target_pile_key = command.split()[-1]
                converter = {
                    "a": 0,
                    "b": 1,
                    "c": 2,
                    "d": 3,
                    "A": 0,
                    "B": 1,
                    "C": 2,
                    "D": 3,
                }
                target_pile = foundation_piles[converter[target_pile_key]].cards

                if target_pile:
                    if (
                        RANKS.index(trans_card.rank)
                        == RANKS.index(target_pile[-1].rank) + 1
                        and trans_card.suit == target_pile[-1].suit
                    ):
                        move_card(initial_pile, target_pile)
                        move_counter.moves += 1
                    else:
                        input(
                            f"Cannot move card {trans_card}"
                            f" to the foundation pile {target_pile_key.upper()}..."
                        )
                else:
                    if trans_card.rank == "A":
                        move_card(initial_pile, target_pile)
                        move_counter.moves += 1
                    else:
                        input("You can only move an Ace to an empty foundation pile...")
            else:
                input("No cards have been drawn from the stockpile...")

        elif match(r"^h$", command):  # Help
            clear_screen()
            commands = Markdown(
                """
- `h` - Display help.
- `p p` - Move cards between piles, where `p` is the name of a pile.
- `s` - Draw a card from the stockpile.
- `ng` - Start a new game.
- `q` - Quit the application."""
            )
            console.print(commands)
            input("\nPress 'Enter' to exit the help...")

        elif match(r"^ng$", command):  # New game
            main()
            break

        else:
            input("The data was entered in an invalid format...")


if __name__ == "__main__":
    main()
