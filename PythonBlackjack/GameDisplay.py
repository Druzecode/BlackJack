import time

from Player import Player
from Card import Card

class GameDisplay:
    def __init__(self):
        self.__min_bet = 5
    
    def show_intro(self):
        word = "BLACKJACK"
        print("\t\t\t\tWelcome To:\n")
        for char in word:
            time.sleep(0.1)
            print("\t" + char, end="", flush=True)
        print("\n")
        for _ in range(10):
            time.sleep(0.02)
            print("\u2663 ", end="", flush=True)
            time.sleep(0.02)
            print("\u2666 ", end="", flush=True)
            time.sleep(0.02)
            print("\u2660 ", end="", flush=True)
            time.sleep(0.02)
            print("\u2665 ", end="", flush=True)
        print("\n")

    def print_game(self, player, house, bet, hole_card=False):
        print("\033c", end="")  # Clear screen
        bet_str = f"Bet: ${bet}"
        print(bet_str, end="")
        money = f" (${player.money})"
        for _ in range(16-len(bet_str)-len(money)):
            print(" ", end="")
        print(money)

        for card in player.hand:
            self.draw_card(card)
        print("")
        print(f"{player.name}: {player.total}\n")

        if house.num_of_cards > 0:
            for card in house.hand:
                if(hole_card and card == house.hand[1]):
                    self.draw_back(card)
                else:
                    self.draw_card(card)
            print("")
            if hole_card:
                print(f"{house.name}: ??\n")
            else:
                print(f"{house.name}: {house.total}\n")

    def draw_back(self, card):  # draws the back of a card (for hold cards)
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

    def draw_card(self, card):  # draws a specific card's picture
        print("\t┌───────────┐")
        print(f"\t│ {card.get_display_rank()}        │")
        print("\t│           │")
        print("\t│           │")
        print("\t│           │")
        print(f"\t│     {card.get_display_suit()}     │")
        print("\t│           │")
        print("\t│           │")
        print("\t│           │")
        print(f"\t│        {card.get_display_rank()} │")
        print("\t└───────────┘")

        print("\t", end="")
        card.display_card_as_text()
        print("\n")