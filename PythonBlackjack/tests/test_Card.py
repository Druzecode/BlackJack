import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from Card import Card


def test_card_defaults():
    card = Card()
    assert card.suit == Card.Suit.index("HEARTS")
    assert card.rank == Card.Rank.index("ACE")

@pytest.mark.parametrize("suits, ranks", [
    (range(0,4), range(0, 13)),
    (["HEARTS", "DIAMONDS", "CLUBS", "SPADES"], ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]),
    (["hearts", "diamonds", "clubs", "spades"], ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]),
    (["hearts", "Diamonds", "cLUbS", "spaDES"], range(0, 13))
])
def test_all_valid_card_values(suits, ranks):
    for s in suits:
        for r in ranks:
            card = Card(s, r)
            assert card.suit == card.get_suit_index(s)
            assert card.rank == card.get_rank_index(r)

@pytest.mark.parametrize("suit, rank, error", [
    (-1, 0, ValueError),
    (4, 14, ValueError),
    ("STARS", "JOKER", ValueError)
])
def test_invalid_card_values(suit, rank, error):
    with pytest.raises(Exception) as excinfo:
        Card(suit, rank)
    assert isinstance(excinfo.value, error)

@pytest.mark.parametrize("rank, flag, value", [
    (0, None, 11),
    (0, True, 1),
    (1, None, 2),
    (2, None, 3),
    (3, None, 4),
    (4, None, 5),
    (5, None, 6),
    (6, None, 7),
    (7, None, 8),
    (8, None, 9),
    (9, None, 10),
    (10, None, 10),
    (11, None, 10),
    (12, None, 10)
])
def test_card_value(rank, flag, value):
    for suit in range(0,4): #do this for each suit to confirm there's no difference in different suits
        assert Card(suit, rank).get_value(flag) == value

@pytest.mark.parametrize("rank, value", [
    (1, "A "),
    (2, "2 "),
    (3, "3 "),
    (4, "4 "),
    (5, "5 "),
    (6, "6 "),
    (7, "7 "),
    (8, "8 "),
    (9, "9 "),
    (10, "10"),
    (11, "J "),
    (12, "Q "),
    (13, "K ")
])
def test_display_rank(rank, value):
    for suit in range(0,4): #do this for each suit to confirm there's no difference in different suits
        assert Card(suit, rank).get_display_rank() == value

@pytest.mark.parametrize("suit, value", [
    (0, '\u2665'), #hearts
    (1, '\u2666'), #diamonds
    (2, '\u2663'), #clubs
    (3, '\u2660') #spades
])
def test_display_rank(suit, value):
    for rank in range(0,13): #do this for each rank to confirm there's no difference
        assert Card(suit, rank).get_display_suit() == value

def test_display_card_as_text():
    print("\n")
    Card().display_card_as_text()  # just ensure no errors are raised

