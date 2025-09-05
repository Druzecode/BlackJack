from enum import Enum

class Card:
    class Suit(Enum):
        HEARTS = 1
        DIAMONDS = 2
        CLUBS = 3
        SPADES = 4

    class Rank (Enum):
        ACE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10
        JACK = 11
        QUEEN = 12
        KING = 13

    @property
    def suit(self):
        return self.__suit

    @property
    def rank(self):
        return self.__rank

    def __init__(self, suit=None, rank=None):
        if(suit is None):
            suit = self.Suit.HEARTS
        if(rank is None):    
            rank = self.Rank.ACE
        
        self.__set_suit(suit)
        self.__set_rank(rank) 
    
    def __set_suit(self, x):  # sets a card's suit
        if isinstance(x, self.Suit):
            self.__suit = x
        elif isinstance(x, str):
            self.__suit = self.Suit[x.upper()]
        else:
            self.__suit = self.Suit(x)

    def __set_rank(self, x):  # sets a card's rank
        if isinstance(x, self.Rank):
            self.__rank = x
        elif isinstance(x, str):
            self.__rank = self.Rank[x.upper()]
        else:
            self.__rank = self.Rank(x)

    def display_card_as_text(self):  # displays a card in text
        print(f"{self.__rank.name} of {self.__suit.name}")

    def get_value(self, flag):  # returns the value of a card
        if self.rank == self.Rank.ACE:
            if flag:  # flag is true if total is over 21, and an Ace must be counted as a 1
                return 1
            else:
                return 11  # by default, aces are counted as 11 originally
        elif self.rank == self.Rank.TWO:
            return 2
        elif self.rank == self.Rank.THREE:
            return 3
        elif self.rank == self.Rank.FOUR:
            return 4
        elif self.rank == self.Rank.FIVE:
            return 5
        elif self.rank == self.Rank.SIX:
            return 6
        elif self.rank == self.Rank.SEVEN:
            return 7
        elif self.rank == self.Rank.EIGHT:
            return 8
        elif self.rank == self.Rank.NINE:
            return 9
        elif self.rank == self.Rank.TEN:
            return 10
        elif self.rank == self.Rank.JACK:
            return 10
        elif self.rank == self.Rank.QUEEN:
            return 10
        elif self.rank == self.Rank.KING:
            return 10
        else:
            return 0

    def get_display_rank(self):  # returns the display value of a card
        if self.rank == self.Rank.ACE:
            return "A "
        elif self.rank == self.Rank.TWO:
            return "2 "
        elif self.rank == self.Rank.THREE:
            return "3 "
        elif self.rank == self.Rank.FOUR:
            return "4 "
        elif self.rank == self.Rank.FIVE:
            return "5 "
        elif self.rank == self.Rank.SIX:
            return "6 "
        elif self.rank == self.Rank.SEVEN:
            return "7 "
        elif self.rank == self.Rank.EIGHT:
            return "8 "
        elif self.rank == self.Rank.NINE:
            return "9 "
        elif self.rank == self.Rank.TEN:
            return "10"
        elif self.rank == self.Rank.JACK:
            return "J "
        elif self.rank == self.Rank.QUEEN:
            return "Q "
        elif self.rank == self.Rank.KING:
            return "K "
        else:
            return "  "

    def get_display_suit(self):
        if self.suit == self.Suit.HEARTS:
            return '\u2665'
        if self.suit == self.Suit.DIAMONDS:
            return '\u2666'
        if self.suit == self.Suit.CLUBS:
            return '\u2663'
        if self.suit == self.Suit.SPADES:
            return '\u2660'
        else:
            return ' '

    def draw_back(self):  # draws the back of a card (for hold cards)
        print("\t┌───────────┐")
        print("\t│***********│")
        print("\t│***********│")
        print("\t│***********│")
        print("\t│***********│")
        print("\t│***********│")
        print("\t│***********│")
        print("\t│***********│")
        print("\t│***********│")
        print("\t│***********│")
        print("\t└───────────┘")

        print("\tHold Card")
        print("\n")

    def draw_card(self):  # draws a specific card's picture
        print("\t┌───────────┐")
        print(f"\t│ {self.get_display_rank()}        │")
        print("\t│           │")
        print("\t│           │")
        print("\t│           │")
        print(f"\t│     {self.get_display_suit()}     │")
        print("\t│           │")
        print("\t│           │")
        print("\t│           │")
        print(f"\t│        {self.get_display_rank()} │")
        print("\t└───────────┘")

        print("\t", end="")
        self.display_card_as_text()
        print("\n")