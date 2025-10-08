
import random
import time
import os

from Card import Card
from Deck import Deck
from Game import Game
from Player import Player
from DispLg import DispLg
from DispSm import DispSm



def main():

    try:
        size = os.get_terminal_size()
        columns = size.columns
        rows = size.lines
    except OSError:
        columns = 80  # default width
        rows = 24     # default height

    #print(f"Columns: {columns}, Rows: {rows}")

    display = DispSm() if columns < 50 else DispLg()
    display.show_intro()
    deck = Deck()
    deck.shuffle()
    game = Game(game_display=display, deck=deck)

    deck.cards[0] = Card(Card.Suit.SPADES, Card.Rank.FIVE)
    deck.cards[1] = Card(Card.Suit.SPADES, Card.Rank.SIX)
    game.play()

if __name__ == "__main__":
    main()