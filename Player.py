import abc
import random
from const import MESSAGES, NAMES
from Deck import Deck

class AbstractPlayer(abc.ABC):
    #Абстрактный игрок принимает карты, позицию, ставка и кол-во очков
    def __init__(self):
        self.cards = []
        self.bet = 0
        self.full_points = 0
        self.money = 100

#Функция, которая отслеживает изменение кол-ва очков
    def change_points(self):
        self.full_points = sum([card.points for card in self.cards])

    # Запрос карты из колоды
    def take_card(self, card):
        self.cards.append(card)
        self.change_points()

#Изменение ставки
    @abc.abstractmethod
    def change_bet(self, max_bet, min_bet):
        pass

    @abc.abstractmethod
    def ask_card(self):
        pass

#Отображение карт
    def print_cards(self):
        print(self, '')
        for card in self.cards:
            print(card)
        print('Всього поитнів: ', self.full_points)


#Игрок делает ставку
class Player(AbstractPlayer):

    def __str__(self):
        return f'Ваші карти'

    def change_bet(self, max_bet, min_bet):
        while True:
            value = int(input('Зробіть вашу ставку: '))
            if value < max_bet and value > min_bet:
                self.bet = value
                self.money -= self.bet
                break
        print('Ваша ставка:', self.bet)

    #Запрос карты для игрока
    def ask_card(self):
        choice = input(MESSAGES.get('ask_card'))
        if choice == 'т':
            return True
        else:
            return False


#Бот генрирует рандомную ставку
class Bot(AbstractPlayer):

    #Максимальное кол-во очков для бота
    def __init__(self):
        super().__init__()
        self.max_points = random.randint(17, 20)
        self.name = NAMES.pop()

    def __str__(self):
        return f'Бот - {self.name}'

    def change_bet(self, max_bet, min_bet):
        self.bet = random.randint(min_bet, max_bet)
        self.money -= self.bet
        print(self, 'дає: ', self.bet)

    # Запрос карты, пока кол-во очков меньше макс.значения
    def ask_card(self):
        if self.full_points < self.max_points:
            return True
        else:
            return False


class Dealer(AbstractPlayer):

    max_points = 17

    def __str__(self):
        return f'Дилер'

    def change_bet(self, max_bet, min_bet):
        raise Exception('Це дилер, від грає без ставок')

    # Запрос карты, пока кол-во очков меньше макс.значения
    def ask_card(self):
        if self.full_points < self.max_points:
            return True
        else:
            return False
