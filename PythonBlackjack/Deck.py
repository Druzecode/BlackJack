import random

from Card import Card

class Deck:
    def __init__(self):
        self.cards = [] # Initialize an empty list to hold Card objects
        self.position = 0  # beginning of deck
        for suit in range(1, 5):
            for rank in range(1, 14):
                card = Card()
                card.set_suit(suit)
                card.set_rank(rank)
                self.cards.append(card)

    def shuffle(self):  # shuffles the deck
        random.shuffle(self.cards)  # Use Python's built-in shuffle function
        self.position = 0  # resets the pointer to the start of the deck

    def display(self, draw_cards=False):  # displays all of the cards in the deck
        for card in self.cards:
            if draw_cards:
                card.draw_card()
            else:
                card.display_card()
            print()
        print("\n\n")

    def send_card(self):  # returns the "top" card on the deck
        self.position += 1  # points to next card
        return self.cards[self.position - 1]  # returns previous card

    def get_position(self):  # returns the position in the deck
        return self.position