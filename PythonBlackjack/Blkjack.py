from Deck import Deck
from Game import Game
from DispSm import DispSm

def main():
    display = DispSm()
    display.show_intro()
    deck = Deck()
    deck.shuffle()
    game = Game(game_display=display, deck=deck)

    # deck.cards[0] = Card(Card.Suit.SPADES, Card.Rank.FIVE)
    # deck.cards[1] = Card(Card.Suit.SPADES, Card.Rank.SIX)
    game.play()

if __name__ == "__main__":
    main()