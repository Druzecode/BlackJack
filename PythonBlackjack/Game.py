import random
import time
import math

from Player import Player
from Deck import Deck
from GameDisplay import GameDisplay

class Game:
    def __init__(self, player=None, house=None, deck=None, game_display=None):
        self.__min_bet = 5
        self.__current_bet = 0
        self._player = player if player is not None else Player()
        self._house = house if house is not None else Player("The House", starting_amount=0)
        self._deck = deck if deck is not None else Deck()
        if(game_display != None and isinstance(game_display, GameDisplay)):
            self._game_display = game_display  
        else:
            self._game_display = GameDisplay()
        self._deck.shuffle()

    @property
    def min_bet(self):
        return self.__min_bet
    
    def play(self):
        while self._player.money >= self.__min_bet:
            if self._deck.position > 40:
                self._deck.shuffle()

            self.__current_bet = self.bet()
            self.deal()
            split = self.play_hand(self._player)
            if split:
                self.split()
            else:
                self.h_play()
                result = self.decision(self._player)
                self.settle(result)  # No need for bet argument in settle

            if(self._player.money < self.__min_bet):
                break
            go = input("Continue (or x to exit)... ")
            print("\033c", end="")  # Clear screen
            if go.lower() == 'x':
                break
        
        print(f"Your final total was: ${self._player.money}")
        print("Thanks for playing!\n")

    def _validate_bet(self, bet):
        try:
            bet = int(bet)
        
            if bet > self._player.money:
                print("You do not have that much money!\n")
            elif bet < self.__min_bet:
                print(f"You must enter a valid bet (minimum ${self.__min_bet})!\n")
            else:
                print()  # Print a newline on successful input
                return True
        except ValueError:
            print("Invalid amount entered\n")
        return False
   
    def bet(self):
        while True:
            print(f"You have ${self._player.money}")
            bet = input("Enter bet: $")
            if self._validate_bet(bet):
                break
        return int(bet)

    def deal(self):
        self.hit(self._player, hole_card=True)
        self.hit(self._player, hole_card=True)
        
        self.hit(self._house, hole_card=True)
        self.hit(self._house, hole_card=True)
        
        self._game_display.print_game(self._player, self._house, self.__current_bet, True)

    def play_hand(self, player):
        cont = True
        split = False
        while cont:
            choice = 2
            cont = False
            
            option_split = False
            option_double = False

            if player.total <= 21 and player.num_of_cards < 5:

                if player.num_of_cards == 2 and player.money >= (self.__current_bet * 2):
                    if player.hand[0].rank == player.hand[1].rank:
                        option_split = True
                    elif player.total == 10 or player.total == 11:
                        option_double = True
                
                while True:
                    print("Would you like to (1)Hit, (2)Stand", end="")
                    if option_split and option_double:
                        print(", (3)Split, or (4)Double Down? ", end="")
                    elif option_split:
                        print(", or (3)Split? ", end="")
                    elif option_double:
                        print(", or (3)Double Down? ", end="")
                    else:
                        print("? ", end="")

                    max_options = 2
                    if option_split:
                        max_options += 1
                    if option_double:
                        max_options += 1
                    
                    choice = self.get_input()
                    print()
                    if 1 <= choice <= 4:
                        break
                    else:
                        print("Please make another selection\n")

            if choice == 1:
                self.hit(player, hole_card=True)
                self._game_display.print_game(player, self._house, self.__current_bet, True)
                cont = True
            elif choice == 3:
                if option_double and not option_split:
                    self.double_down(player)
                else:
                    split = True
                cont = False
            elif choice == 4:
                self.double_down(self.__current_bet)
                cont = False
        return split

    def get_input(self):
        try:
            return int(input())
        except ValueError:
            return 0

    def hit(self, player, hole_card=False):
        player.get_card(self._deck.get_top_card())
        if(player == self._player or player == self._house):
            self._game_display.print_game(self._player, self._house, self.__current_bet, hole_card)
        else:
            self._game_display.print_game(player, self._house, self.__current_bet, hole_card)

        time.sleep(.5)

    def split(self):
        player2 = Player(self._player.name + "(second)", 0)
        player2.hand.append(self._player.hand.pop())
        player1 = Player(self._player.name + "(first)", 0)
        player1.hand.append(self._player.hand.pop())
        
        self.hit(player1, hole_card=True)
        self.play_hand(player1)
        self.hit(player2, hole_card=True)
        self.play_hand(player2)
        self.h_play(player2)

        print(f"First Hand: {player1.total} - ", end="")
        result1 = self.decision(player1)
        print(f"Second Hand: {player2.total} - ", end="")
        result2 = self.decision(player2)
        self.settle(result1 + result2)

    def double_down(self, player):
        self.hit(player, hole_card=True)
        self.__current_bet *= 2

    def h_play(self, player=None):
        if player is None:
            player = self._player
        while True:
            self._game_display.print_game(player, self._house, self.__current_bet)
            time.sleep(.5)
            print(f"{self._house.name} chooses to ", end="")
            if self._house.total < 17:
                print("hit\n")
                time.sleep(.5)
                self._house.get_card(self._deck.get_top_card())
                cont = True
            else:
                print("stand\n")
                break

    def decision(self, player):
        time.sleep(.5)

        if player.total <= 21 and player.num_of_cards == 5 and self._house.num_of_cards!= 5:
            print("You Win! (five card rule)")
            return self.__current_bet
        if self._house.total <= 21 and self._house.num_of_cards == 5 and player.num_of_cards!= 5:
            print("You Lose (five card rule)")
            return (self.__current_bet * -1)
        if player.total == 21 and player.num_of_cards == 2:
            if self._house.total == 21 and self._house.num_of_cards == 2:
                print("Draw")
                return 0
            else:
                print("You have a Blackjack!  You Win!")
                return math.ceil(self.__current_bet * 1.5)
        if self._house.total == 21 and self._house.num_of_cards == 2:
            print("The House has a Blackjack! You Lose")
            return (self.__current_bet * -1)
        
        #player or house is over 21
        if player.total > 21:
            print("You are over! ", end="")
        if self._house.total > 21:
            print("House is over! ", end="")
        if player.total > 21 and self._house.total > 21:
            print("Draw")
            return 0
        if player.total > 21 and self._house.total <= 21:
            print("You Lose")
            return (self.__current_bet * -1)
        if self._house.total > 21 and player.total <= 21:
            print("You Win!")
            return self.__current_bet
        
        if self._house.total < player.total:
            print("You Win!")
            return self.__current_bet
        if self._house.total > player.total:
            print("You Lose")
            return (self.__current_bet * -1)
        # if self._house.total == player.total and player.num_of_cards < self._house.num_of_cards:
        #     print("You Win! (Fewer Cards)")
        #     return self.__current_bet
        # if self._house.total == player.total and player.num_of_cards > self._house.num_of_cards:
        #     print("You Lose (House has fewer cards)")
        #     return (self.__current_bet * -1)
        if self._house.total == player.total:
            print("Draw")
            return 0
        else:
            print("Error in decision logic")
            return 0

    def settle(self, result):
        print(f"Result: {result}")
        self._player.settle_bet(result)
        self._player.reset_hand()
        self._house.reset_hand()
        self.__current_bet = 0
        
