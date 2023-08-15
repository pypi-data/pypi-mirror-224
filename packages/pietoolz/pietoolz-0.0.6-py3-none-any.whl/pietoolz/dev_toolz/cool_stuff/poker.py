from __future__ import annotations
from typing import Any, Optional, Union
import random as r





class Card:
    """
    Card class.
    """
    _suit: str
    _rank: str
    _writing: Optional[str]


    RANK_STRS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                 'J', 'Q', 'K'
                ]
    SUIT_STRS = ['spade', 'spades', 's',
                'heart', 'hearts', 'h',
                'diamond', 'diamonds', 'd',
                'club', 'clubs', 'c'
                ]
    SUIT_EMOJIS = {'s': '♠',
                   'h': '♥',
                   'd': '♦',
                   'c': '♣'
                  }


    def __init__(self, suit: str, rank: int) -> None:
        """
        >>> c1 = Card('h', 13)
        >>> c1._suit
        '♥'
        >>> c1._rank
        'K'
        >>> c2 = Card('heart', 1)
        """
        # Error checks
        if suit.lower() not in self.SUIT_STRS:
            raise InvalidSuitException
        if rank not in range(1, 14):
            raise InvalidRankException
        # init
        self._suit = self.SUIT_EMOJIS[suit.lower()[0]]
        self._rank = self.RANK_STRS[rank-1]
    
    
    def get_suit(self):
        pass


    def get_rank(self):
        pass


    def write_feltpen(self):
        pass
        

class Deck:
    """
    Standard 52-card deck.
    
    Optional Parameter
    ------------------
    jokers=0
        Enter integers 1 or 2, for the number of joker cards to add
        to the 52-card deck.

    Pre-Condition
    -------------
    - <jokers> must be either 0, 1, or 2. Otherwise, an exception will
      be raised.
    
    Client Code
    -----------
    # >>> my_deck = Deck()
    # >>> my_deck.get_joker_count()
    # 0
    # >>> another_deck = Deck(jokers=1)
    # >>> another_deck.get_joker_count()
    # 1
    # >>> another_deck = Deck(jokers=2)
    # >>> another_deck.get_joker_count()
    # 2
    >>> 

    Dev Representation Invariants
    -----------------------------
    - Inbetween method calls, the instance fields <_ordered_deck> and
      <_unordered_deck> must share the same number of cards remaining in the
      Deck. I.e., the two instance fields are two different representations
      of the current status of the Deck.
    """
    _joker_count: int
    _ordered_deck: list[Card]
    _unordered_deck: dict[str, list[str]]
    

    def __init__(self, jokers=0) -> None:
        """
        #TODO
        """
        self._joker_count = jokers
        self._unordered_deck = {
            'heart': ['1']          #TODO
        }


    def _update_deck(self):
        """
        Update both deck representations.

        Dev Code
        --------
        >>> #TODO
        """
        pass


    def get_joker_count(self):
        pass


class Poker(Deck):
    """
    Parent class for different variations of the poker game.
        First Betting Round: Players fold, call, or raise in turn.

    Betting Rounds:
        Pre-flop: Initial round described in "Starting."
        Flop: After three community cards are revealed.
        Turn: After fourth community card is revealed.
        River: After fifth community card is revealed.

    Community Cards:
        Flop: First three cards, face up.
        Turn: Fourth card, face up.
        River: Fifth card, face up.

    Combination:
        Use five of seven cards (two private, five community).
        Form best hand: High Card, Pair, Two Pair, etc.

    Winning:
        Best Hand: Highest-ranking hand wins pot.
        Last Player: Remaining player if others fold.
        Tie: Split pot if hands are equal.

    Hand Rankings (Highest to Lowest):
        Royal Flush
        Straight Flush
        Four of a Kind
        Full House
        Flush
        Straight
        Three of a Kind
        Two Pair
        One Pair
        High Card

    This hierarchy covers the essential rules and structure of Texas Hold'em.

    Happy Playing!
    """
    pass


class InvalidSuitException(Exception):
    def __init__(self):
        super().__init__("<suit> must be 's', 'h', 'd', or 'c'.")


class InvalidRankException(Exception):
    def __init__(self):
        super().__init__("<rank> must be an integer member of [1, 13].")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
