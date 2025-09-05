import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from Player import Player
from Deck import Deck

@pytest.mark.parametrize("input", [
    ("test"),
    ("Player1"),
    ("")
])
def test_player_default_initialization(monkeypatch, input):
    monkeypatch.setattr('builtins.input', lambda _: input)
    player = Player()
    if(input != None and len(input) > 0 ):
        assert player.name == input
    else:
        assert player.name == "Player1"
    assert player.money == 100
    assert player.num_of_cards == 0
    assert player.hand == []

@pytest.mark.parametrize("name, amount", [
    ("test", 50)
])
def test_player_initialization(name, amount):
    player = Player(name, amount)
    assert player.name == name
    assert player.money == amount
    assert player.num_of_cards == 0
    assert player.hand == []

def test_player_hand():
    player = Player("Player1")
    assert player.num_of_cards == 0
    assert player.hand == []
    
    #deal two cards and verify them
    deck = Deck()
    deck.shuffle()
    player.get_card(deck)
    assert player.num_of_cards == 1
    assert player.hand[0] == deck.cards[0]
    player.get_card(deck)
    assert player.num_of_cards == 2
    assert player.hand[1] == deck.cards[1]
    
    player.display_cards()  # Just ensure it runs without error
    player.reset_hand()
    assert player.num_of_cards == 0

def test_player_money():
    player = Player("Player1")
    assert player.money == 100
    player.win_amount(50);
    assert player.money == 150
    player.lose_amount(25);
    assert player.money == 125