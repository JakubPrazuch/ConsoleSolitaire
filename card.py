from typing import Final
from types import MappingProxyType


RANKS: Final = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
SUITS: Final = MappingProxyType(
    {
        "hearts": "\033[31m♥\033[0m",
        "diamonds": "\033[31m♦\033[0m",
        "clubs": "\033[36m♣\033[0m",
        "spades": "\033[36m♠\033[0m",
    }
)


class Card:
    def __init__(self, rank: str, suit: str, *, face_down: bool = True) -> None:
        # Rank
        if rank not in RANKS:
            raise ValueError(f"invalid rank: '{rank}'")
        self.rank = rank

        # Suit
        if suit not in SUITS:
            raise ValueError(f"invalid suit: '{suit}'")
        self.suit = suit
        self.suit_symbol = SUITS[suit]

        # Suit color
        red_suits = ("hearts", "diamonds")
        self.suit_color = "red" if self.suit in red_suits else "black"

        self.face_down = face_down

    def can_move_to_column(self, target_column: list["Card"]) -> bool:
        if not target_column:
            return self.rank == "K"
        return (
            self.suit_color != target_column[-1].suit_color  # Suits color differences
            and RANKS.index(self.rank) == RANKS.index(target_column[-1].rank) - 1
        )

    def __str__(self) -> str:
        return f"{self.rank}{self.suit_symbol}"

    def display(self) -> str:
        if self.face_down:
            return "[ ]"
        return (
            f"{self.rank}"
            f"{self.suit_symbol if self.rank == '10' else self.suit_symbol + ' '}"
        )
