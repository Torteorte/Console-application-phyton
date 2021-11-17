class Menu:
    def __init__(self, players, points, trump):
        self.players = players
        self.points = points
        self.trump_of_game = trump
        self.menu_number = None

    def handler_call_menu(self, def_of_game):
        self.set_number()
        self.__checkout_number(def_of_game)

    def set_number(self):
        self.menu_number = input('Выберите один из следующих пунктов: \n '
                                 '1. Просмотреть карты игроков \n '
                                 '2. Просмотреть очки игроков \n '
                                 '3. Начать новую игру \n '
                                 '4. Глянуть козырь \n '
                                 '5. Закончить игру \n')

    def __checkout_number(self, def_of_game):
        if self.menu_number == '1':
            self.__show_players_by_numbers()

        elif self.menu_number == '2':
            self.__show_players_points()

        elif self.menu_number == '3':
            self.__new_game(def_of_game)

        elif self.menu_number == '4':
            self.__show_game_trump()

        elif self.menu_number == '5':
            self.__end_game()
            return

        else:
            print('Шутки со мной шутишь?')

        self.handler_call_menu(def_of_game)

    def __show_players_by_numbers(self):
        for player in range(len(self.players)):
            print(self.players[player])

    def __show_players_points(self):
        print(self.points)

    def __show_game_trump(self):
        print('Козырь: ', self.trump_of_game)

    @staticmethod
    def __new_game(def_of_game):
        def_of_game()

    @staticmethod
    def __end_game():
        print('Спасибо за игру')
