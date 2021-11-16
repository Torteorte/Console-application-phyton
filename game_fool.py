from game import Game
from menu import Menu
from utils import input_players, set_cards, set_trump


def game():
    game_fool = Game(input_players(), set_cards(), set_trump())
    game_fool.cards_for_players()
    game_fool.sort_points()

    print('Козырь: ', game_fool.trump)
    for key in game_fool.sorted_players_points:
        print(key + ':', game_fool.ui_players_carts[key])
    print(game_fool.list_of_players)

    menu = Menu(game_fool.list_of_players, game_fool.sorted_players_points)
    menu.set_number(game)


print(game())
