from random import randrange
from player import Player
from utils import sort_list
from constants import cards_per_player_in_durak


class Game:
    def __init__(self, players, list_of_cards, trump):
        self.players = players
        self.list_of_cards = list_of_cards
        self.trump = trump
        self.list_of_players = []
        self.sorted_list = []
        self.sorted_points = {}
        self.dict_of_points = {}

    def get_data_for_game(self):
        self.__create_list_of_players()
        self.__calculate_players_points()
        self.__get_sorted_players()

    def __create_list_of_players(self):
        for index in range(self.players):
            player = Player('Игрок' + str(index + 1))
            self.__give_cards_to_player(player)
            self.list_of_players.append(player)

    def __give_cards_to_player(self, player):
        for j in range(cards_per_player_in_durak):
            length = len(self.list_of_cards)
            number_card = randrange(length)
            player.add_card(self.list_of_cards[number_card])
            self.list_of_cards.remove(self.list_of_cards[number_card])

    def __calculate_players_points(self):
        for player in self.list_of_players:
            self.__get_nominals_of_cards_with_trump(player.cards)
            player.get_points()

    def __get_nominals_of_cards_with_trump(self, player_cards):
        for card in player_cards:
            card.set_nominal(self.trump)

    def __get_sorted_players(self):
        for player in self.list_of_players:
            self.sorted_list.append(player)
            self.dict_of_points[player.player_number] = player.points
            self.sorted_points = dict(sorted(self.dict_of_points.items(), key=lambda item: item[1], reverse=True))
        sort_list(self.sorted_list)

    def show_sorted_players_cards(self):
        for index in range(len(self.sorted_list)):
            print(self.sorted_list[index])
