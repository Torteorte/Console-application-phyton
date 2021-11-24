from random import randrange
from constants.constants import card_suit, cards_names
from core.Card import CardForDurak


def get_game_trump():
    return card_suit[int(randrange(4))]


def get_deck_of_cards_for_durak():
    deck_of_cards = []
    for name in cards_names:
        for suit in card_suit:
            card = CardForDurak(suit, name)
            deck_of_cards.append(card)
    return deck_of_cards


def get_users_who_will_play_durak_game():
    try:
        number_of_players = int(input('Выберите колличество игроков от 2 до 6: '))
        if number_of_players <= 1:
            print('Слишком мало игроков.')
            return get_users_who_will_play_durak_game()

        elif number_of_players > 6:
            print('Всем не хватит карт.')
            return get_users_who_will_play_durak_game()

        return number_of_players

    except ValueError:
        print('(╯° □ °)╯ ┻━━┻ : это не число!')
        return get_users_who_will_play_durak_game()
