import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from Game import Game
from Player import Player
from Deck import Deck

def test_game_initialization():
    game = Game()
    assert game.min_bet == 5

@pytest.mark.parametrize("balance, amount, expected", [
    (10, 5, True),
    (10, 10, True),
    (10, 11, False),
    (10, 101, False),
    (100, 3, False),
    (100, "abc", False),
    (100, "", False),
    ("100", 100, True),
    ("10", 100, True),
    ("asfd", 100, True),
    ("100", 101, False),
])
def test_validate_bet(balance, amount, expected):
    player = Player("TestPlayer", balance)
    game = Game(player=player)
    actual = game._validate_bet(amount)
    assert actual == expected

def test_game_bet(monkeypatch):
    game = Game()
    monkeypatch.setattr('builtins.input', lambda _: "11")
    bet = game.bet()
    assert bet == 11

def test_game_deal():
    player = Player("TestPlayer")
    deck = Deck()
    game = Game(player=player, deck=deck)  #init includes deck shuffle
    game.deal()
    assert player.num_of_cards == 2 
    assert player.hand[0] == deck.cards[0]
    assert player.hand[1] == deck.cards[1]
    