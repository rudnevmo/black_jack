import Player
from const import MESSAGES
from Deck import Deck
import random

class Game():
    max_pl_count = 4

#Конструктор игры, здесь хранятся боты, игрок, кол-во игроков, колода, диапазон ставок
    def __init__(self):
        self.players = []
        self.player = None
        self.player_pos = None
        #self.dealler = None
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 0

# Protected метод, который даёт запрос на начало игры и возвращает бул
    @staticmethod
    def _ask_starting(message):
        while True:
            choice = input(message)
            if choice == 'н':
                return False
            elif choice == 'т':
                return True

#Запрос кол-ва ботов, проверка на макс кол-во
    def _launching(self):
        while True:
            bots_count = int(input('Привіт! Введи кількість противників -> '))
            if bots_count <= self.max_pl_count - 1:
                break
        self.all_players_count = bots_count + 1 #кол-во игроков с нами

        #По кол-ву генерирует ботов из класса бот и добавляем игрока
        for _ in range(bots_count):
            b = Player.Bot()
            self.players.append(b)
            print(b, ' створено')
        self.player = Player.Player()
        self.player_pos = random.randint(0, self.all_players_count)
        print('Ваша позиція - ', self.player_pos)
        self.players.insert(self.player_pos, self.player)

#Запрос или генерация ставки у каждого игрока
    def ask_bet(self):
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)

#Первая раздача карт
    def fiest_descr(self):
        for player in self.players:
            player.ask_card(self.deck, 2)

#Метод ссылается на запрос о начале игры и запускает её
    def start_game(self):
        message = MESSAGES.get('ask_start')
        if not self._ask_starting(message=message):
            exit(1)

        self._launching()

        self.ask_bet()

        self.fiest_descr()
