import Player
from const import MESSAGES
from Deck import Deck
import random

class Game():

    def __init__(self):
        self.players = []
        self.player = None
        #self.dealler = None
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 0
        pass

    @staticmethod
    def _ask_starting(message):
        while True:
            choice = input(message)
            if choice == 'н':
                return False
            elif choice == 'т':
                return True


    def _launching(self):
        bots_count = int(input('Привіт! Введи кількість противників -> '))
        self.all_players_count = bots_count + 1
        for i in range(bots_count):
            b = Player.Bot(position=i)
            self.players.append(b)
            print(b, ' створено')
        self.player = Player.Player(position=bots_count + 1)
        self.players.append(self.player)

    def ask_bet(self):
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)


    def fiest_descr(self):
        for player in self.players:
            player.ask_card(self.deck, 2)

    def start_game(self):
        message = MESSAGES.get('ask_start')
        if not self._ask_starting(message=message):
            exit(1)

        self._launching()

        self.ask_bet()

        self.fiest_descr()
