class Player:
    player_number = ''
    cards = []
    points = 0

    def set(self, player_number, cards):
        self.player_number = player_number
        self.cards = cards

    def set_points(self, points):
        self.points = points
