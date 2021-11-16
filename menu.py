class Menu:
    menu_number = 0

    def __init__(self, players, points):
        self.players = players
        self.points = points

    def set_number(self, def_game):
        self.menu_number = input('Выберите один из следующих пунктов: \n '
                                 '1. Просмотреть карты игроков \n '
                                 '2. Просмотреть очки игроков \n '
                                 '3. Начать новую игру \n '
                                 '4. Закончить игру \n')
        self.__checkout_number(def_game)

    def __checkout_number(self, def_game):
        if self.menu_number == '1':
            for key in self.players:
                print(key.player_number + ':', key.cards)
            self.set_number(def_game)
        elif self.menu_number == '2':
            print(self.points)
            self.set_number(def_game)
        elif self.menu_number == '3':
            def_game()
        elif self.menu_number == '4':
            print('Спасибо за игру')
        else:
            print('Шутки со мной шутишь?')
            self.set_number(def_game)
