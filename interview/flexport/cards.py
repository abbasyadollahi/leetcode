"""
I have 2G cards and a wallet with 3G, 4B.
Can you buy a R card which costs 5G?
Yes I can buy the R card, spending 3G tokens and using the 2G cards I own as discount.
After purchasing, I have 2G, 1R cards and a bank of 4B.
"""

from dataclasses import dataclass
from enum import Enum


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


@dataclass(frozen=True)
class Card:
    color: Color
    cost: dict[Color, int]


class User:
    def __init__(self, cards: list[Card], wallet: dict[Color, int]) -> None:
        self.cards = cards
        self.coupons = dict.fromkeys(list(Color), 0)
        self.wallet = dict.fromkeys(list(Color), 0)

        for card in cards:
            self.coupons[card.color] += 1

        for color, count in wallet.items():
            self.wallet[color] += count

    def afford_card(self, card: Card) -> bool:
        return all(cost <= self.wallet[color] + self.coupons[color] for color, cost in card.cost.items())

    def purchase_card(self, card: Card) -> bool:
        if not self.afford_card(card):
            return False

        for color, cost in card.cost.items():
            self.wallet[color] -= max(0, cost - self.coupons[color])

        self.add_card(card)

        return True

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        self.coupons[card.color] += 1


# Abbas
abbas = User(cards=[], wallet={Color.RED: 5})

card1 = Card(Color.BLUE, {Color.RED: 2, Color.GREEN: 2})

assert abbas.purchase_card(card1) is False
assert card1 not in abbas.cards
assert abbas.coupons == {Color.RED: 0, Color.GREEN: 0, Color.BLUE: 0}
assert abbas.wallet == {Color.RED: 5, Color.GREEN: 0, Color.BLUE: 0}

# John
john = User(
    cards=[Card(Color.GREEN, {}), Card(Color.GREEN, {})],
    wallet={Color.GREEN: 3, Color.BLUE: 4},
)

card2 = Card(Color.RED, {Color.GREEN: 5})
card3 = Card(Color.RED, {Color.GREEN: 2})

assert john.purchase_card(card2) is True
assert card2 in john.cards
assert john.coupons == {Color.RED: 1, Color.GREEN: 2, Color.BLUE: 0}
assert john.wallet == {Color.RED: 0, Color.GREEN: 0, Color.BLUE: 4}

assert john.purchase_card(card3) is True
assert card3 in john.cards
assert john.coupons == {Color.RED: 2, Color.GREEN: 2, Color.BLUE: 0}
assert john.wallet == {Color.RED: 0, Color.GREEN: 0, Color.BLUE: 4}
