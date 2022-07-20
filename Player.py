import abc
import random
from Deck import Deck

class AbstractPlayer(abc.ABC):
    #Абстрактный игрок принимает карты, позицию, ставка и кол-во очков
    def __init__(self):
        self.cards = []
        self.bet = 0
        self.full_points = 0

#Функция, которая отслеживает изменение кол-ва очков
    def change_points(self):
        self.full_points = sum([card.points for card in self.cards])

#Запрос карты из колоды
    def ask_card(self, deck, card_count):
        for _ in range(card_count):
            card = deck.get_card()
            self.cards.append(card)
        self.change_points()
        return True

#Изменение ставки
    @abc.abstractmethod
    def change_bet(self, max_bet, min_bet):
        pass

#Отображение карт
    def print_cards(self):
        print(self, 'bot data')
        for card in self.cards:
            print(card)
        print(self.full_points)

#Игрок делает ставку
class Player(AbstractPlayer):
    def change_bet(self, max_bet, min_bet):
        while True:
            value = int(input('Зробіть вашу ставку: '))
            if value < max_bet and value > min_bet:
                self.bet = value
                break
        print('Ваша ставка:', self.bet)


class Dealler(AbstractPlayer):
    pass

#Бот генрирует рандомную ставку
class Bot(AbstractPlayer):
    def change_bet(self, max_bet, min_bet):
        self.bet = random.randint(min_bet, max_bet)
        print(self, 'дає: ', self.bet)
