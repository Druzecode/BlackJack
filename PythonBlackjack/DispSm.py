import time

from DispLg import DispLg

class DispSm(DispLg):
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
        self._print_symbols()
        for char in word:
            time.sleep(0.02)
            print(char, end="",flush=True)
        print("\n", end="")
        self._print_symbols()
        print("\n", end="", flush=True)
    
    def print_game(self, player, house=None, bet=None, hole_card=False):
        print("\033c", end="")  # Clear screen
        bet_str = "Bet: " + str(bet)
        print(bet_str, end="")
        money = " $" + str(player.money)
        for _ in range(16-len(bet_str)-len(money)):
            print(" ", end="")
        print(money)

        #Draw player cards
        for card in player.hand:
            print("┌──┐", end="")
        print("")
        for card in player.hand:
            print ("│" + card.get_display_rank() + "│", end="")
        print("")
        for card in player.hand:
            print ("│ " + card.get_display_suit() + "│", end="")
        print("")
        for card in player.hand:
            print("└──┘", end="")
        print("")
        print(player.name + ": " + str(player.total) + "\n")

        #Draw house cards
        if house != None and house.num_of_cards > 0:
            for card in house.hand:
                print("┌──┐", end="")
            print("")
            for card in house.hand:
                if(hole_card and len(house.hand) > 1 and card == house.hand[1]):
                    print ("│**│", end="")
                else:
                    print ("│" + card.get_display_rank() + "│", end="")
            print("")
            for card in house.hand:
                if(hole_card and len(house.hand) > 1 and card == house.hand[1]):
                    print ("│**│", end="")
                else:
                    print ("│ " + card.get_display_suit() + "│", end="")
            print("")
            for card in house.hand:
                print("└──┘", end="")
            print("")
            if hole_card:
                print(house.name + " showing " + house.hand[0].get_display_rank() + "\n")
            else:
                print(house.name + ": " + str(house.total) + "\n")
  
    def draw_back(self, card):  # draws the back of a card (for hold cards)
        print("\t┌──┐")
        print("\t│**│")
        print("\t│**│")
        print("\t└──┘")

        print("\tHold Card")
        print("\n")

    def draw_card(self, card):  # draws a specific card's picture
        print("\t┌──┐")
        print("\t│" + card.get_display_rank() + " │")
        print("\t│ " + card.get_display_suit() + "│")
        print("\t└──┘")

        print("\t", end="")
        card.display_card_as_text()
        print("\n")