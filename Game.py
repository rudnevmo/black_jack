import Player
import random
from const import MESSAGES
from Deck import Deck


class Game:
    max_pl_count = 4

# Конструктор игры, здесь хранятся боты, игрок, кол-во игроков, колода, диапазон ставок
    def __init__(self):
        self.players = []
        self.player = None
        self.player_pos = None
        self.dealer = Player.Dealer()
        self.all_players_count = 1
        self.deck = None
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
            bots_count = int(input('Введи кількість противників -> '))
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
    def firest_descr(self):
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)
        card = self.deck.get_card()
        self.dealer.take_card(card)
        self.dealer.print_cards()

#проверка условий окончания игры
    def check_stop(self, player):
        if player.full_points >= 21:
            return True
        else:
            return False

    def remove_player(self, player):
        player.print_cards()
        if isinstance(player, Player.Player):
            print('Ти програв!')
        elif isinstance(player, Player.Bot):
            print(player, 'програв!')
        self.players.remove(player)

    # Игра спрашивает у каждого игрока нужна ли ему карта, если то игрок - печатает его карты
    def ask_cards(self):
        for player in self.players:
            while player.ask_card():
                card = self.deck.get_card()
                player.take_card(card)
                is_stop = self.check_stop(player)
                if is_stop:
                    if player.full_points > 21 or isinstance(player, Player.Player):
                        self.remove_player(player)
                    break
                if isinstance(player, Player.Player):
                    player.print_cards()

    def check_winner(self):
        if self.dealer.full_points > 21:
            print('Ділер програв! Усі гравці перемогли!')
            for winner in self.players:
                winner.money += winner.bet * 2
        else:
            for player in self.players:
                if player.full_points == self.dealer.full_points:
                    player.money += player.bet
                    print(MESSAGES.get('eq').format(player=player, points=player.full_points))
                elif player.full_points > self.dealer.full_points or player.full_points == 21:
                    player.money += player.bet * 2
                    if isinstance(player, Player.Bot):
                        print(MESSAGES.get('win').format(player))
                    elif isinstance(player, Player.Player):
                        print('Ти переміг!')
                elif player.full_points < self.dealer.full_points:
                    if isinstance(player, Player.Bot):
                        print(MESSAGES.get('lose').format(player))
                    elif isinstance(player, Player.Player):
                        print('Ти програв!')

    def play_with_dealler(self):
        while self.dealer.ask_card():
            card = self.deck.get_card()
            self.dealer.take_card(card)
        self.dealer.print_cards()

# Метод ссылается на запрос о начале игры и запускает её
    def start_game(self):
        message = MESSAGES.get('ask_start')
        if not self._ask_starting(message=message):
            exit(1)

        #генерация даных для старта
        self._launching()
        while True:
            self.full_points = 0
            self.deck = Deck()
            #запрос ставки
            self.ask_bet()

            #раздача начальных карт игроков
            self.firest_descr()

            #вывод карт после раздачи
            self.player.print_cards()

            #запрос на ещё одну карту
            self.ask_cards()

            #игра с диллером
            self.play_with_dealler()

            self.check_winner()

            if not self._ask_starting(MESSAGES.get('rerun')):
                break

