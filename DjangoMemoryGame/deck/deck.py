import random

from DjangoMemoryGame.cards.cards import Card


class Deck(object):

    matched_cards = []

    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']

        for i in range(8):
            self.cards.append(Card(suits[i//2]))
        self.shuffle_cards()

    def shuffle_cards(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def print_cards(self):
        return [self.cards[i].print_card_face_up() if self.cards[i].face_up else self.cards[i].print_card_face_down(i)
                for i in range(len(self.cards))]
