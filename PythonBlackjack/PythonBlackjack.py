
import random
import time

from Card import Card
from Deck import Deck
from Game import Game
from Player import Player

def intro():
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

def main():
    intro()
    deck = Deck()
    deck.shuffle()
    player = Player()
    house = Player("The House")
    game = Game()

    while player.money >= game.min_bet:
        if deck.get_position() > 40:
            deck.shuffle()

        bet = game.bet(player)
        game.deal(player, deck, False)
        game.deal(house, deck, True)

        split = game.choice(player, deck, bet)
        if split:
            game.split(player, house, deck, bet)
        else:
            game.h_play(house, deck)
            game.decision(player, house, bet)
            game.settle(player, house)  # No need for bet argument in settle

        go = input("Would you like to continue (y/n)? ")
        print("\033c", end="")  # Clear screen
        if go.lower()!= 'y':
            break

    print(f"Your final total was: ${player.money}")
    print("Thanks for playing\n")

if __name__ == "__main__":
    main()