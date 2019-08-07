
# start game - show all cards in table, render two inputs for which cards to open and add button to send request
# turn cards over and they are the same, same player continues else next player selects cards
# when all cards are turned over stop game, remove input fields and print winner and show Restart button
from django.shortcuts import render

from DjangoMemoryGame.app import Game


def start_game(request):
    return render(request, 'index.html')

