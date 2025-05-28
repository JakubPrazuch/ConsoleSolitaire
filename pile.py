from card import Card


class Stockpile:
    def __init__(self, cards: list[Card]) -> None:
        self.face_down_cards = cards
        self.face_up_cards: list[Card] = []

    def display(self) -> str:
        face_down_cards_repr = "[ ]" if self.face_down_cards else "{ }"

        if self.face_up_cards:
            top_card = self.face_up_cards[-1]
            top_card.face_down = False
            face_up_cards_repr = top_card.display()
        else:
            face_up_cards_repr = "{ }"

        return f"{face_down_cards_repr} {face_up_cards_repr}"


class FoundationPile:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def display(self) -> str:
        if self.cards:
            self.cards[-1].face_down = False
            return self.cards[-1].display()
        return "{ }"


class Column:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def find(self, card: Card) -> Card | None:
        """Searches for a card in the column.

        Args:
            card (Card): The card to be found.

        Returns:
            Card | None: Returns the card from the column if found, otherwise 'None'.
        """
        for comparison_card in self.cards:
            if card.rank == comparison_card.rank and card.suit == comparison_card.suit:
                return comparison_card
        return None

    def move_cards(self, target_set: list[Card], card_index: int) -> None:
        """Move cards between columns.

        Args:
            target_set (list[Card]): _description_
            card_index (int): _description_
        """
        while card_index < len(self.cards):
            card = self.cards.pop(card_index)
            target_set.append(card)

    def display(self) -> str:
        if self.cards:
            self.cards[-1].face_down = False  # The last card is face up
            return " ".join(card.display() for card in self.cards)
        return ""


def move_card(
    initial_pile: list[Card], target_pile: list[Card], card_index: int = -1
) -> None:
    card = initial_pile.pop(card_index)
    target_pile.append(card)
