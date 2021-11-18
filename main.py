from core.GameDurak import GameDurak
from core.Menu import Menu
from utils.utils import get_users_who_will_play_durak_game, get_deck_of_cards_for_durak, get_game_trump


def init_game():
    number_of_players = get_users_who_will_play_durak_game()
    deck_of_cards = get_deck_of_cards_for_durak()
    trump = get_game_trump()

    game_durak = GameDurak(number_of_players, deck_of_cards, trump)

    return game_durak


def init_menu(game_durak):
    list_of_players = game_durak.list_of_players
    sorted_players = game_durak.sorted_by_points_players
    trump = game_durak.trump

    menu = Menu(list_of_players, sorted_players, trump, start_durak)

    return menu


def start_durak():
    game_durak = init_game()
    game_durak.play_the_game()

    menu = init_menu(game_durak)
    menu.handler_call_menu()


print(start_durak())
