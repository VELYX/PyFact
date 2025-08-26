import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        cards = [(rank, suit) for suit in self.SUITS for rank in self.RANKS]
        tuple(cards)
        self.__cards = cards

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if len(self.__cards) < 1:
            return None   
        else:
            card = self.__cards.pop()
            return card
    
    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"

