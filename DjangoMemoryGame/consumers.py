import asyncio
import json
from channels.consumer import AsyncConsumer

from DjangoMemoryGame.app import Game
from DjangoMemoryGame.players.player import Player


class GameConsumer(AsyncConsumer):

    app = None
    current_player = None
    player_one = None
    player_two = None

    async def websocket_connect(self, event):
        await self.send({
            'type': 'websocket.accept'
        })

        cards = self.start_game()
        self.create_players()
        self.current_player = self.player_one

        await self.update_ui(cards)

    async def websocket_receive(self, event):
        text = event.get('text', None)
        if text is not None:
            loaded_data = json.loads(text)

        if self.app:
            card_one = int(loaded_data['card_one'])
            card_two = int(loaded_data['card_two'])
            self.app.turn_cards_over(card_one, card_two)
            cards = self.app.deck.print_cards()
            self.current_player.matches += 1

            await self.update_ui(cards)

            is_same_cards = self.app.check_if_cards_are_same(card_one, card_two)
            if not is_same_cards:
                await asyncio.sleep(2)
                self.current_player.matches -= 1

                if self.current_player == self.player_one:
                    self.current_player = self.player_two
                else:
                    self.current_player = self.player_one

                cards = self.app.deck.print_cards()
                await self.update_ui(cards)

        if self.is_game_finished():
            await self.send(
                {
                    "type": "websocket.close"
                }
            )

    async def update_ui(self, cards):
        await self.send({
            "type": "websocket.send",
            "text": json.dumps(
                {
                    'current_player': self.current_player.name,
                    'data': json.dumps(cards)
                }
            )
        })

    def start_game(self):
        self.app = Game()
        return self.app.deck.print_cards()

    def create_players(self):
        self.player_one = Player('Player 1')
        self.player_two = Player('Player 2')

    def is_game_finished(self):
        total_matches = self.player_one.matches + self.player_two.matches
        if total_matches == len(self.app.deck.cards) // 2:
            return True
        return False
