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
def test_player_default_initialization(monkeypatch, name):
    monkeypatch.setattr('builtins.input', lambda _: "Player1")
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
    player.win_amount(50)
    assert player.money == 150
    player.lose_amount(25)
    assert player.money == 125

@pytest.mark.parametrize("cards, expected", [
    (["ACE", "KING"], 21),
    (["ACE", "KING", "TEN"], 21),
    (["ACE", "KING", "TEN", "FIVE"], 26),
    (["ACE", "EIGHT", "ACE"], 20),
    (["ACE", "NINE", "ACE"], 21),
    (["TEN", "ACE", "ACE"], 12),
    (["ACE", "TEN", "ACE"], 12),
    (["ACE", "ACE", "TEN"], 12),
    (["ACE", "ACE"], 12),
    (["ACE", "ACE", "ACE", "ACE"], 14),
    (["QUEEN", "ACE", "ACE", "ACE", "ACE"], 14),
    (["QUEEN", "JACK", "ACE", "ACE", "ACE"], 23)
])
def test_player_total(cards, expected):
    player = Player("Player1")
    deck = Deck()
    for c in cards:
        player.get_card(Card("CLUBS", c))
    assert player.total == expected
