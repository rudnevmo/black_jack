from const import PRINTED, SUITS, RANKS
from random import shuffle
from itertools import product

class Card():
    def __init__(self, suit, rank, picture, points):
        self.suit = suit
        self.rank = rank
        self.picture = picture
        self.points = points

    def __str__(self):
        message = self.picture + '\nPoints: ' + str(self.points)
        return message


class Deck():

    def __init__(self):
        self.cards = self._generete_deck()
        shuffle(self.cards)


    def _generete_deck(self):
        cards = []
        for suit, rank in product(SUITS, RANKS):
            if rank == 'ace':
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10
            picture = PRINTED.get(rank)
            c = Card(suit=suit, rank=rank, points=points, picture=picture)
            cards.append(c)
        return cards

    def get_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
