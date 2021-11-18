from random import randrange
from core.Player import Player
from constants.constants import cards_per_player_in_durak


class GameDurak:
    def __init__(self, number_of_players, deck_of_cards, trump):
        self.number_of_players = number_of_players
        self.deck_of_cards = deck_of_cards
        self.trump = trump
        self.list_of_players = []
        self.sorted_by_points_players = []

    def create_data_for_game(self):
        self.create_list_of_players()
        self.calculate_players_points()
        self.update_sorted_players()

    def create_list_of_players(self):
        for index in range(self.number_of_players):
            player = Player('Игрок' + str(index + 1))

            self.give_cards_to_player(player)
            self.list_of_players.append(player)

    def give_cards_to_player(self, player):
        for index_iteration in range(cards_per_player_in_durak):
            length_of_deck_of_cards = len(self.deck_of_cards)
            number_card = randrange(length_of_deck_of_cards)

            player.add_card(self.deck_of_cards[number_card])
            self.deck_of_cards.remove(self.deck_of_cards[number_card])

    def calculate_players_points(self):
        for player in self.list_of_players:
            self.get_nominals_of_cards_with_trump(player.cards)
            player.calc_points()

    def get_nominals_of_cards_with_trump(self, player_cards):
        for card in player_cards:
            card.update_nominal_by_trump(self.trump)

    def update_sorted_players(self):
        self.sorted_by_points_players = sorted(self.list_of_players, key=lambda player: player.points, reverse=True)

    def show_sorted_players_cards(self):
        for player in self.sorted_by_points_players:
            print(player.player_number, player.cards)

    def play_the_game(self):
        self.create_data_for_game()
        print('Козырь: ', self.trump)
        self.show_sorted_players_cards()
