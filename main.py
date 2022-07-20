from Deck import Deck
from Game import Game
# Игра Блекжек
if __name__ == '__main__':
    g = Game()
    g.start_game()

    for pl in g.players:
        pl.print_cards()
        print('***********')

    print(g.player_pos)
    print(g.players)

    #d = Deck()

    #print(len(d))
    #card = d.get_card()
    #print(card)
    #print(len(d))