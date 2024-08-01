import random


def createDeck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(f'{suit}: {rank}')

    return deck


class Deck:

    def __init__(self):
        self.game_deck = createDeck()
        random.shuffle(self.game_deck)
