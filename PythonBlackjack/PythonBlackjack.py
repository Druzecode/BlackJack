
import random
import time
import os

from Card import Card
from Deck import Deck
from Game import Game
from Player import Player
from GameDisplay import GameDisplay
from GameDisplayTI import GameDisplayTI



def main():

    try:
        size = os.get_terminal_size()
        columns = size.columns
        rows = size.lines
    except OSError:
        columns = 80  # default width
        rows = 24     # default height

    print(f"Columns: {columns}, Rows: {rows}")


    display = GameDisplay()
    display.ShowIntro()
    
    deck = Deck()
    deck.shuffle()
    player = Player()
    house = Player("The House", starting_amount=0)
    game = Game()

    game.play(deck, player, house)

    print(f"Your final total was: ${player.money}")
    print("Thanks for playing\n")

if __name__ == "__main__":
    main()