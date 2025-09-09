import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from Player import Player
from Deck import Deck
from Card import Card

@pytest.mark.parametrize("name", [
    ("test"),
    ("Player1"),
    (""),
    (None)
])
def test_player_default_initialization(name):
    player = Player(name)
    if(name != None and len(name) > 0 ):
        assert player.name == name
    else:
        assert player.name == "Player1"
    assert player.money == 100
    assert player.num_of_cards == 0
    assert player.hand == []

@pytest.mark.parametrize("name, amount, expected", [
    ("test", 50, 50),
    ("test", "50", 100),
    ("test", "a", 100),
    ("test", None, 100)
])
def test_player_initialization(name, amount, expected):
    player = Player(name, amount)
    assert player.name == name
    assert player.money == expected
    assert player.num_of_cards == 0
    assert player.hand == []

def test_player_hand():
    player = Player("Player1")
    assert player.num_of_cards == 0
    assert player.hand == []
    
    #deal two cards and verify them
    deck = Deck()
    deck.shuffle()
    player.get_card(deck.get_top_card())
    assert player.num_of_cards == 1
    assert player.hand[0] == deck.cards[0]
    player.get_card(deck.get_top_card())
    assert player.num_of_cards == 2
    assert player.hand[1] == deck.cards[1]
    
    player.reset_hand()
    assert player.num_of_cards == 0

def test_player_money():
    player = Player("Player1")
    assert player.money == 100
    player.win_amount(50);
    assert player.money == 150
    player.lose_amount(25);
    assert player.money == 125

def test_player_total():
    player = Player("Player1")
    deck = Deck()
    player.get_card(Card(Card.Suit.DIAMONDS, Card.Rank.ACE))
    player.get_card(Card(Card.Suit.DIAMONDS, Card.Rank.KING))
    assert player.total == 21
    player.get_card(Card(Card.Suit.DIAMONDS, Card.Rank.TEN))
    assert player.total == 21
    player.get_card(Card(Card.Suit.DIAMONDS, Card.Rank.FIVE))
    assert player.total == 26