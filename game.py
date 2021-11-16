from random import randrange
from player import Player
from utils import card_to_number, sum_of_cards, sort_points


class Game:
    sorted_players_points = []
    ui_players_carts = {}

    def __init__(self, players, list_of_cards, trump):
        self.players = players
        self.list_of_cards = list_of_cards
        self.trump = trump
        self.list_of_players = []

    def cards_for_players(self):
        for index in range(self.players):
            player_cards = []
            for j in range(6):
                length = len(self.list_of_cards)
                number_card = randrange(length)
                player_cards.append(self.list_of_cards[number_card])
                self.list_of_cards.remove(self.list_of_cards[number_card])
            player = Player('Игрок' + str(index + 1), player_cards)
            self.ui_players_carts[player.player_number] = player_cards
            self.list_of_players.append(player)

    def sort_points(self):
        players_points = {}
        for player in self.list_of_players:
            points_of_cards = []
            for number_of_card in range(6):
                item_card = player.cards[number_of_card]
                item_name = item_card.name
                item_nominal = card_to_number(item_name)
                item_card.set_nominal(self.trump, item_nominal)
                points_of_cards.append(item_card.nominal)
            players_points[player.player_number] = sum_of_cards(points_of_cards)
            player.points = sum_of_cards(points_of_cards)
        self.sorted_players_points = sort_points(players_points)
