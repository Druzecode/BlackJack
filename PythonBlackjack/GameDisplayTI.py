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

    def show_intro(self):
        word = "   BLACKJACK!"
        print("  Welcome To:")
        self._print_symbols();
        for char in word:
            time.sleep(0.02)
            print(char, end="",flush=True)
        print("\n", end="")
        self._print_symbols();
        print("\n", end="", flush=True)
    
    def print_game(self, player, house=None, bet=None, hole_card=False):
        print("\033c", end="")  # Clear screen
        bet_str = f"Bet: ${bet}"
        print(bet_str, end="")
        money = f" (${player.money})"
        for _ in range(16-len(bet_str)-len(money)):
            print(" ", end="")
        print(money)

        #Draw player cards
        for card in player.hand:
            print("┌──┐", end="")
        print("")
        for card in player.hand:
            print (f"│{card.get_display_rank()}│", end="")
        print("")
        for card in player.hand:
            print (f"│ {card.get_display_suit()}│", end="")
        print("")
        for card in player.hand:
            print("└──┘", end="")
        print("")
        print(f"{player.name}: {player.total}\n")

        #Draw house cards
        if house != None and house.num_of_cards > 0:
            for card in house.hand:
                print("┌──┐", end="")
            print("")
            for card in house.hand:
                if(hole_card and len(house.hand) > 1 and card == house.hand[1]):
                    print ("│**│", end="")
                else:
                    print (f"│{card.get_display_rank()}│", end="")
            print("")
            for card in house.hand:
                if(hole_card and len(house.hand) > 1 and card == house.hand[1]):
                    print ("│**│", end="")
                else:
                    print (f"│ {card.get_display_suit()}│", end="")
            print("")
            for card in house.hand:
                print("└──┘", end="")
            print("")
            if hole_card:
                print(f"{house.name} showing {house.hand[0].get_display_rank()}\n")
            else:
                print(f"{house.name}: {house.total}\n")
        
    
    def draw_back(self, card):  # draws the back of a card (for hold cards)
        print("\t┌──┐")
        print("\t│**│")
        print("\t│**│")
        print("\t└──┘")

        print("\tHold Card")
        print("\n")

    def draw_card(self, card):  # draws a specific card's picture
        print("\t┌──┐")
        print(f"\t│{card.get_display_rank()} │")
        print(f"\t│ {card.get_display_suit()}│")
        print("\t└──┘")

        print("\t", end="")
        card.display_card_as_text()
        print("\n")