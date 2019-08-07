
class Card:

    face_up = False

    def __init__(self, suit):
        self.suit = suit

    def print_card_face_up(self):
        return '{}'.format(self.suit)

    def print_card_face_down(self, position):
        return 'Card {}'.format(position + 1)
