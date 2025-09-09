import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from Deck import Deck

def test_deck_initialization():
    deck = Deck()
    assert deck.position == 0
    assert deck.validate_deck() == True

@pytest.mark.parametrize("iterations", [
    (1),
    (2),
    (10),
    (100)
])
def test_deck_shuffle(iterations):
    deck = Deck()
    for _ in range(iterations):
        last_shuffle = deck.cards.copy()
        deck.shuffle()
        assert deck.validate_deck() == True
        assert deck.cards != last_shuffle  # After shuffle, order should be different

def test_deck_position():
    deck = Deck()
    cards1 = deck.cards.copy()
    deck.shuffle()
    assert deck.cards != cards1  # After shuffle, order should be different

@pytest.mark.parametrize("iterations", [
    (1),
    (10),
    (52),
    (53),
    (100)
])
def test_deck_multiple_shuffles(iterations):
    deck = Deck()
    deck.shuffle()
    drawn_cards = []
    for _ in range(iterations):
        if deck.position < 52:
            card = deck.get_top_card()
            assert card == deck.cards[deck.position - 1]
            assert card not in drawn_cards
            drawn_cards.append(card)
            
        else:
            assert len(drawn_cards) == 52
            with pytest.raises(IndexError):
                deck.get_top_card()
            