from random import randrange
from constants import card_suit, cards_names
from card import CardForDurak


def get_game_trump():
    return card_suit[int(randrange(4))]


def get_list_of_all_cards_for_durak():
    all_cards = []
    for name in cards_names:
        for suit in card_suit:
            card = CardForDurak(suit, name)
            all_cards.append(card)
    return all_cards


def get_users_who_will_play_durak_game():
    number_of_players = int(input('Выберите колличество игроков от 2 до 6: '))
    if number_of_players <= 1:
        number_of_players = int(input('Слишком мало игроков. \n '
                                      'Выберите колличество игроков от 2 до 6: '))
    elif number_of_players > 6:
        number_of_players = int(input('Всем не хватит карт. \n '
                                      'Выберите колличество игроков от 2 до 6: '))
    return number_of_players


def sum_of_cards(player_cards):
    summa = 0
    for card in player_cards:
        summa += card.nominal
    return summa


def sort_list(game_list):
    for index in range(len(game_list)):
        prev_i = index - 1
        if game_list[index].points > game_list[prev_i].points:
            game_list[prev_i], game_list[index] = game_list[index], game_list[prev_i]
