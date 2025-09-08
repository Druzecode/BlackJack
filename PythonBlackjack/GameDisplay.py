import time

from Player import Player
from Card import Card

class GameDisplay:
    def __init__(self):
        self.__min_bet = 5
    
    def ShowIntro(self):
        word = "BLACKJACK"
        print("\t\t\t\tWelcome To:\n")
        for char in word:
            time.sleep(0.15)
            print("\t" + char, end="", flush=True)
        print("\n")
        for _ in range(10):
            time.sleep(0.05)
            print("\u2663 ", end="", flush=True)
            time.sleep(0.05)
            print("\u2666 ", end="", flush=True)
            time.sleep(0.05)
            print("\u2660 ", end="", flush=True)
            time.sleep(0.05)
            print("\u2665 ", end="", flush=True)
        print("\n")

    def PrintGame(self, player, house, bet, initial_deal=False):
        print("\033c", end="")  # Clear screen
        bet_str = f"Bet: ${bet}"
        print(bet_str, end="")
        money = f" (${player.money})"
        for _ in range(16-len(bet_str)-len(money)):
            print(" ", end="")
        print(money)

        for card in player.hand:
            card.draw_card()
        print("")
        print(f"{player.name}: {player.total}\n")

        if house.num_of_cards > 0:
            for card in house.hand:
                if(initial_deal and card == house.hand[1]):
                    card.draw_back()
                else:
                    card.draw_card()
            print("")
            if initial_deal:
                print(f"{house.name}: ??\n")
            else:
                print(f"{house.name}: {house.total}\n")
