from game import Game
from menu import Menu
from utils import get_users_who_will_play_durak_game, get_list_of_all_cards_for_durak, get_game_trump


def init_game():
    players = get_users_who_will_play_durak_game()
    cards_for_game = get_list_of_all_cards_for_durak()
    trump = get_game_trump()
    game_fool = Game(players, cards_for_game, trump)
    game_fool.get_data_for_game()
    return game_fool


def init_menu(game_fool):
    players = game_fool.list_of_players
    points = game_fool.sorted_points
    trump = game_fool.trump
    menu = Menu(players, points, trump)
    return menu


def start_durak():
    game_fool = init_game()

    print('Козырь: ', game_fool.trump)
    game_fool.show_sorted_players_cards()

    menu = init_menu(game_fool)
    menu.handler_call_menu(start_durak)


print(start_durak())
