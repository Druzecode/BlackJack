import random

from Card import Card

class Deck:
    def __init__(self):
        self.__cards = [] # Initialize an empty list to hold Card objects
        self.__position = 0  # beginning of deck
        count =0
        for suit in range(0, 4):
            for rank in range(0, 13):
                card = Card(suit, rank)
                self.__cards.append(card)
                count = count + 1

    @property
    def cards(self):
        return self.__cards
    
    @property
    def position(self):
        return self.__position

    def shuffle(self):  # shuffles the deck
        random.shuffle(self.__cards)  # Use Python's built-in shuffle function
        self.__position = 0  # resets the pointer to the start of the deck

    def get_top_card(self):  # returns the "top" card on the deck
        self.__position += 1  # points to next card
        if(self.__position > len(self.__cards)):
            raise IndexError("No more cards in the deck")
        return self.__cards[self.__position - 1]  # returns previous card

    def validate_deck(self):  # Validates that the deck has 52 unique cards
        if len(self.__cards) != 52:
            return False
        seen = set()
        for card in self.__cards:
            combo = (card.suit, card.rank)
            if combo in seen:
                return False
            seen.add(combo)
        return True