Suit = [
    "HEARTS",
    "DIAMONDS",
    "CLUBS",
    "SPADES"
]

Rank = [
    "ACE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE",
    "TEN",
    "JACK",
    "QUEEN",
    "KING"
]
class Card:
    @property
    def suit(self):
        return self.__suit

    @property
    def rank(self):
        return self.__rank

    def __init__(self, suit=None, rank=None):
        if suit is None:
            suit = 0  # default to hearts
        if rank is None:
            rank = 0  # default to ACE (index 0)
        self.__set_suit(suit)
        self.__set_rank(rank)

    def get_suit_index(self, value):
        if isinstance(value, str):
            return Suit.index(value.upper())
        elif isinstance(value, int) and value >= 0 and value < 4:
            return value
        else:
            raise ValueError("Suit must be an integer between 1 and 4 or a valid suit name")

    def get_rank_index(self, value):
        if isinstance(value, str):
            return Rank.index(value.upper())
        elif isinstance(value, int) and 0 <= value < 13:
            return value
        else:
            raise ValueError("Rank must be an integer between 0 and 12 or a valid rank name")

    def __set_suit(self, x):  # sets a card's suit
        self.__suit = self.get_suit_index(x)

    def __set_rank(self, x):
        self.__rank = self.get_rank_index(x)

    def display_card_as_text(self):  # displays a card in text
        print(Rank[self.__rank] + " of " + Suit[self.__suit])

    def get_value(self, flag):  # returns the value of a card
        # Returns the value of a card
        if self.rank == 0:  # ACE
            return 1 if flag else 11
        elif 1 <= self.rank <= 8:  # TWO to NINE
            return self.rank + 1
        elif 9 <= self.rank <= 12:  # TEN, JACK, QUEEN, KING
            return 10
        else:
            return 0

    def get_display_rank(self, short=False):  # returns the display value of a card
        if self.rank == 0:
            return "A" if short else "A "
        elif 1 <= self.rank <= 8:
            return str(self.rank + 1) if short else str(self.rank + 1) + " "
        elif self.rank == 9:
            return "T" if short else "10"
        elif self.rank == 10:
            return "J" if short else "J "
        elif self.rank == 11:
            return "Q" if short else "Q "
        elif self.rank == 12:
            return "K" if short else "K "
        else:
            return " " if short else "  "

    def get_display_suit(self):
        if self.suit == Suit.index("HEARTS"):
            return '\u2665'
        if self.suit == Suit.index("DIAMONDS"):
            return '\u2666'
        if self.suit == Suit.index("CLUBS"):
            return '\u2663'
        if self.suit == Suit.index("SPADES"):
            return '\u2660'
        else:
            return ' '