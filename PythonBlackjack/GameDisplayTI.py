import time

from GameDisplay import GameDisplay
from Player import Player
from Card import Card

class GameDisplayTI(GameDisplay):
    def __init__(self):
        self.__min_bet = 5
        self.__width = 16
        self.__height = 8
    

    def _print_symbols(self):
        for _ in range(4):
            time.sleep(0.02)
            print("\u2663", end="", flush=True)
            time.sleep(0.02)
            print("\u2666", end="", flush=True)
            time.sleep(0.02)
            print("\u2660", end="", flush=True)
            time.sleep(0.02)
            print("\u2665", end="", flush=True)
        print("\n", end="")

    def ShowIntro(self):
        word = "   BLACKJACK!"
        print("  Welcome To:")
        self._print_symbols();
        for char in word:
            time.sleep(0.02)
            print(char, end="",flush=True)
        print("\n", end="")
        self._print_symbols();
        print("\n", end="", flush=True)
    