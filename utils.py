from random import randrange
from constants import card_suit, cards_names
from card import Card


def set_trump():
    return card_suit[int(randrange(4))]


def set_cards():
    all_cards = []
    for name in cards_names:
        for suit in card_suit:
            card = Card(suit, name)
            all_cards.append(card)
    return all_cards


def input_players():
    number_of_players = int(input('Выберите колличество игроков от 1 до 6: '))
    if number_of_players < 1:
        number_of_players = int(input('Слишком мало игроков. \n '
                                      'Выберите колличество игроков от 1 до 6: '))
    elif number_of_players > 6:
        number_of_players = int(input('Всем не хватит карт. \n '
                                      'Выберите колличество игроков от 1 до 6: '))
    return number_of_players


def card_to_number(cards_list):
    nominal = 11 if cards_list == 'B' else \
        12 if cards_list == 'Q' else \
        13 if cards_list == 'K' else \
        14 if cards_list == 'A' else int(cards_list)
    return nominal


def sum_of_cards(cards):
    summa = 0
    for card_nominal in range(6):
        summa += cards[card_nominal]
    return summa


def sort_points(players_points):
    sorted_values = sorted(players_points.values(), reverse=True)
    sorted_players_points = {}

    for points in sorted_values:
        for player in players_points.keys():
            if players_points[player] == points:
                sorted_players_points[player] = players_points[player]
                break
    return sorted_players_points

