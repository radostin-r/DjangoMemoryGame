from DjangoMemoryGame.deck.deck import Deck


class Game(object):

    def __init__(self):
        self.deck = Deck()
        self.players = None

    def switch_players(self):
        return

    def turn_cards_over(self, card_one, card_two):
        # card_one and card_two are the positions of the cards in the deck
        if not isinstance(card_one, int) or not isinstance(card_two, int):
            raise Exception('Wrong input for which card to turn over.')
        if card_one in self.deck.matched_cards or card_two in self.deck.matched_cards:
            raise Exception('Selected card is already turned over.')
        card_one -= 1
        card_two -= 1

        if self.deck.cards[card_one].face_up or self.deck.cards[card_one].face_up:
            return
        self.deck.cards[card_one].face_up = True
        self.deck.cards[card_two].face_up = True

    def check_if_cards_are_same(self, card_one, card_two):
        if self.deck.cards[card_one-1].suit != self.deck.cards[card_two-1].suit:
            self.deck.cards[card_one-1].face_up = False
            self.deck.cards[card_two-1].face_up = False
            return False
        return True
