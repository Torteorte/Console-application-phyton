from random import randrange
from game import Game
from player import Player
from menu import Menu

card_suit = ['♠', '♣', '♦', '♥']
cards_names = ['6', '7', '8', '9', '10', 'B', 'Q', 'K', 'A']
menu = Menu()
fool_game = Game()
print('Козырь: ', fool_game.trump)

def set_players():
    number_of_players = int(input('Выберите колличество игроков от 1 до 6: '))
    if number_of_players < 1:
        number_of_players = int(input('Слишком мало игроков. \n '
                                      'Выберите колличество игроков от 1 до 6: '))
    elif number_of_players > 6:
        number_of_players = int(input('Всем не хватит карт. \n '
                                      'Выберите колличество игроков от 1 до 6: '))
    return number_of_players


def card_to_number(cards_list, card_trump, game_trump):
    nominal = 11 if cards_list == 'B' else \
        12 if cards_list == 'Q' else \
        13 if cards_list == 'K' else \
        14 if cards_list == 'A' else int(cards_list)

    # TODO: Вынести
    return nominal + 9 if card_trump == game_trump else nominal


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


def game():
    players = set_players()
    list_of_cards = []
    all_players_cards = {}
    list_of_players = []
    players_points = {}

    game_trump = card_suit[int(randrange(4))]
    print('Козырь: ', game_trump)

    for name in cards_names:
        for suit in card_suit:
            list_of_cards.append({suit: name})

    for index in range(players):
        player_cards = []
        for j in range(6):
            length = len(list_of_cards)
            number_card = randrange(length)
            player_cards.append(list_of_cards[number_card])
            list_of_cards.remove(list_of_cards[number_card])
        player = Player()
        player.set('player' + str(index + 1), player_cards)
        list_of_players.append(player)
        all_players_cards[player.player_number] = player.cards

    for player in list_of_players:
        points_of_cards = []
        for number_of_card in range(6):
            for card_trump in player.cards[number_of_card]:
                card = player.cards[number_of_card][card_trump]
                points_of_cards.append(card_to_number(card, card_trump, game_trump))
        players_points[player.player_number] = sum_of_cards(points_of_cards)
        player.points = sum_of_cards(points_of_cards)

    sorted_players_points = sort_points(players_points)

    for key in sorted_players_points:
        print(key + ':', all_players_cards[key])

    menu.set(all_players_cards, sorted_players_points)
    menu.set_number(game)


print(game())
