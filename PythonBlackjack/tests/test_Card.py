import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from Card import Card

def compare_enum(member, value):
    if(isinstance(value, int)):
        return member.value == value
    elif(isinstance(value, str)):
        return member.name == value.upper()
    else:
        return member == value

def test_card_defaults():
    card = Card()
    assert card.suit == Card.Suit.HEARTS
    assert card.rank == Card.Rank.ACE

@pytest.mark.parametrize("suits, ranks", [
    (range(1,5), range(1, 14)),
    (["HEARTS", "DIAMONDS", "CLUBS", "SPADES"], ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]),
    (["hearts", "diamonds", "clubs", "spades"], ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]),
    (["hearts", "Diamonds", "cLUbS", "spaDES"], range(1, 14))
])
def test_all_valid_card_values(suits, ranks):
    for s in suits:
        for r in ranks:
            card = Card(s, r)
            assert compare_enum(card.suit, s)
            assert compare_enum(card.rank, r)

@pytest.mark.parametrize("suit, rank, error", [
    (0, 0, ValueError),
    (5, 14, ValueError),
    ("STARS", "JOKER", KeyError)
])
def test_invalid_card_values(suit, rank, error):
    with pytest.raises(Exception) as excinfo:
        Card(suit, rank)
    assert isinstance(excinfo.value, error)

@pytest.mark.parametrize("rank, flag, value", [
    (1, None, 11),
    (1, True, 1),
    (2, None, 2),
    (3, None, 3),
    (4, None, 4),
    (5, None, 5),
    (6, None, 6),
    (7, None, 7),
    (8, None, 8),
    (9, None, 9),
    (10, None, 10),
    (11, None, 10),
    (12, None, 10),
    (13, None, 10)
])
def test_card_value(rank, flag, value):
    for suit in range(1,5): #do this for each suit to confirm there's no difference in different suits
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
    for suit in range(1,5): #do this for each suit to confirm there's no difference in different suits
        assert Card(suit, rank).get_display_rank() == value

@pytest.mark.parametrize("suit, value", [
    (1, '\u2665'), #hearts
    (2, '\u2666'), #diamonds
    (3, '\u2663'), #clubs
    (4, '\u2660') #spades
])
def test_display_rank(suit, value):
    for rank in range(1,14): #do this for each rank to confirm there's no difference
        assert Card(suit, rank).get_display_suit() == value

def test_display_card_as_text():
    print("\n")
    Card().display_card_as_text()  # just ensure no errors are raised

