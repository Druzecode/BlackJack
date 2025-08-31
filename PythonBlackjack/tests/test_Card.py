import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from Card import Card

def test_card_defaults():
    card = Card()
    card.display_card()
    assert card.suit == Card.Suit.HEARTS
    assert card.rank == Card.Rank.ACE
    card.display_card()

def test_set_card_values():
    card = Card()
    card.set_suit(Card.Suit.SPADES)
    card.set_rank(Card.Rank.KING)
    assert card.suit == Card.Suit.SPADES
    assert card.rank == Card.Rank.KING
    card.display_card()

def test_set_card_invalid_values():
    card = Card()
    #with pytest.raises(ValueError):
    card.set_suit("InvalidSuit")
    with pytest.raises(ValueError):
        card.set_rank(20)  # Invalid rank
    assert card.suit == Card.Suit.HEARTS
    assert card.rank == Card.Rank.ACE
    card.display_card()