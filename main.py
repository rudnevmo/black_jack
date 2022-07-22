from Deck import Deck
from Game import Game
from const import MESSAGES
from Player import Bot
# Игра Блекжек
if __name__ == '__main__':
    g = Game()
    g.start_game()

    print(g.player.money)
