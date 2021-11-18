class Menu:
    def __init__(self, list_of_players, sorted_players, trump, create_game):
        self.list_of_players = list_of_players
        self.sorted_players = sorted_players
        self.trump_of_game = trump
        self.menu_number = None
        self.create_game = create_game

    def handler_call_menu(self):
        self.select_menu_number()
        self.checkout_number()

    def select_menu_number(self):
        self.menu_number = input('Выберите один из следующих пунктов: \n '
                                 '1. Просмотреть карты игроков \n '
                                 '2. Просмотреть очки игроков \n '
                                 '3. Начать новую игру \n '
                                 '4. Глянуть козырь \n '
                                 '5. Закончить игру \n')

    def checkout_number(self):
        if self.menu_number == '1':
            self.show_players_by_numbers()

        elif self.menu_number == '2':
            self.show_players_points()

        elif self.menu_number == '3':
            self.start_new_game()

        elif self.menu_number == '4':
            self.show_game_trump()

        elif self.menu_number == '5':
            self.end_game()
            exit()

        else:
            print('Шутки со мной шутишь?')

        return self.handler_call_menu()

    def show_players_by_numbers(self):
        for player in range(len(self.list_of_players)):
            print(self.list_of_players[player])

    def show_players_points(self):
        for player in self.sorted_players:
            print(str(player.player_number) + ':', player.points)

    def show_game_trump(self):
        print('Козырь: ', self.trump_of_game)

    def start_new_game(self):
        self.create_game()

    @staticmethod
    def end_game():
        print('Спасибо за игру')
