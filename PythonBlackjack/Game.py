import random
import time

from Player import Player

class Game:
    def __init__(self):
        self.min_bet = 5

    def bet(self, player):
        while True:
            print(f"You currently have ${player.money}")
            try:
                bet = int(input("How much would you like to bet? $"))
                if bet > player.money:
                    print("You do not have that much money!\n")
                elif bet < self.min_bet:
                    print(f"You must enter a valid bet (minimum ${self.min_bet})!\n")
                else:
                    print()  # Print a newline on successful input
                    break
            except ValueError:
                print("Invalid amount entered\n")
        return bet

    def deal(self, player, deck, hide_card):
        print(f"{player.name} has: ")
        card1 = deck.send_card()
        card1.draw_card()
        player.hand.append(card1)
        player.num_of_cards += 1

        card2 = deck.send_card()
        if hide_card:
            card2.draw_back()
        else:
            card2.draw_card()
        player.hand.append(card2)
        player.num_of_cards += 1

        time.sleep(3)
        print("\033c", end="")  # Clear screen

    def choice(self, player, deck, bet):
        cont = True
        split = False
        while cont:
            player.total = 0
            choice = 0
            flag = False
            cont = False
            print("\033c", end="")  # Clear screen
            print(f"{player.name}, you have the: ")
            for card in player.hand:
                print("\t", end="")
                card.display_card()
                player.total += card.get_value(flag)
            if player.total > 21:
                player.total = 0
                flag = True
                for card in player.hand:
                    player.total += card.get_value(flag)

            print(f"\nYou have a total of: {player.total}\n")

            if player.total <= 21 and player.num_of_cards < 5:
                if player.hand.rank == player.hand.rank and player.num_of_cards == 2 and player.money >= (bet * 2):
                    if player.total == 10 or player.total == 11:
                        while True:
                            print("Would you like to (1)Hit, (2)Stand, (3)Split, or (4)Double Down? ")
                            choice = self.get_input()
                            print()
                            if 1 <= choice <= 4:
                                break
                            else:
                                print("Please make another selection\n")
                    else:
                        while True:
                            print("Would you like to (1)Hit, (2)Stand, or (3)Split? ")
                            choice = self.get_input()
                            print()
                            if 1 <= choice <= 3:
                                break
                            else:
                                print("Please make another selection\n")
                elif player.hand.rank!= player.hand.rank and (player.total == 10 or player.total == 11) and player.num_of_cards == 2:
                    while True:
                        print("Would you like to (1)Hit, (2)Stand, or (3)Double Down? ")
                        choice = self.get_input()
                        print()
                        if 1 <= choice <= 3:
                            break
                        else:
                            print("Please make another selection\n")
                    if choice == 3:
                        choice = 4
                else:
                    while True:
                        print("Would you like to (1)Hit or (2)Stand? ")
                        choice = self.get_input()
                        print()
                        if 1 <= choice <= 2:
                            break
                        else:
                            print("Please make another selection\n")
            else:
                choice = 2

            if choice == 1:
                self.hit(player, deck)
                cont = True
            elif choice == 3:
                split = True
                cont = False
            elif choice == 4:
                self.double_down(player, deck, bet)
                cont = False
        return split

    def get_input(self):
        try:
            return int(input())
        except ValueError:
            return 0

    def hit(self, player, deck):
        print("\033c", end="")  # Clear screen
        print(f"{player.name} received the ")
        new_card = deck.send_card()
        new_card.draw_card()
        player.hand.append(new_card)
        player.num_of_cards += 1
        time.sleep(2)
        print("\033c", end="")  # Clear screen

    def split(self, player, house, deck, bet):
        player2 = Player(player.name + "'s second hand", 0)
        player2.hand.append(player.hand.pop())
        player.num_of_cards -= 1
        player2.num_of_cards += 1
        self.hit(player, deck)
        self.hit(player2, deck)
        self.choice(player, deck, bet)
        self.choice(player2, deck, bet)
        self.h_play(house, deck)
        print("First Hand:")
        self.decision(player, house, bet)
        print("Second Hand:")
        self.decision(player2, house, bet)
        player.money += player2.money
        self.settle(player, house, bet)

    def double_down(self, player, deck, bet):
        self.hit(player, deck)
        bet *= 2
        flag = player.total == 11
        player.total += player.hand[-1].get_value(flag)

    def h_play(self, house, deck):
        cont = True
        while cont:
            house.total = 0
            flag = False
            cont = False
            print("\033c", end="")  # Clear screen
            print(f"{house.name} has the: ")
            for card in house.hand:
                print("\t", end="")
                card.display_card()
                house.total += card.get_value(flag)
            if house.total > 21:
                house.total = 0
                flag = True
                for card in house.hand:
                    house.total += card.get_value(flag)

            print(f"\n{house.name} has a total of: {house.total}, and chooses to ", end="")
            if house.total < 17:
                print("hit\n")
                time.sleep(2.5)
                self.hit(house, deck)
                cont = True
            else:
                print("stand\n")

    def decision(self, player, house, bet):
        print(f"You have a total of {player.total}\n")
        time.sleep(2)

        if player.total < 21 and player.num_of_cards == 5 and house.num_of_cards!= 5:
            print("You Win! (five card rule)\n")
            player.money += bet
        elif house.total < 21 and house.num_of_cards == 5 and player.num_of_cards!= 5:
            print("You Lose (five card rule)\n")
            player.money -= bet
        else:
            if player.total == 21 and player.num_of_cards == 2:
                if house.total!= 21 or house.num_of_cards > 2:
                    print("You have a Blackjack!\nYou Win!\n")
                    player.money += (bet * 1.5)
                else:
                    print("Draw\n")
            elif house.total == 21 and house.num_of_cards == 2:
                print("The House has a Blackjack!\nYou Lose\n")
                player.money -= bet
            else:
                if player.total > 21:
                    print("You are over!")
                if house.total > 21:
                    print("House is over!")
                if player.total > 21 and house.total > 21:
                    print("Draw\n")
                elif player.total > 21 and house.total <= 21:
                    print("You Lose\n")
                    player.money -= bet
                elif house.total > 21 and player.total <= 21:
                    print("You Win!\n")
                    player.money += bet
                elif house.total <= 21 and player.total <= 21:
                    if house.total < player.total:
                        print("You Win!\n")
                        player.money += bet
                    elif house.total > player.total:
                        print("You Lose\n")
                        player.money -= bet
                    else:
                        if player.num_of_cards < house.num_of_cards:
                            print("You Win! (Fewer Cards)\n")
                            player.money += bet
                        elif player.num_of_cards > house.num_of_cards:
                            print("You Lose (House has fewer cards)\n")
                            player.money -= bet
                        else:
                            print("Draw\n")

    def settle(self, player, house, bet=0):  # bet parameter is optional and defaults to 0
        player.num_of_cards = 0
        house.num_of_cards = 0
        # No need to reset bet here, as it's passed by value

    def go_play(self):
        go = input("Would you like to continue (y/n)? ")
        print("\033c", end="")  # Clear screen
        return go.lower() == 'y'  # Return True if the player wants to continue, False otherwise