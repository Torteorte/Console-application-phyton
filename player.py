class Player:
    points = 0

    def __init__(self, player_number, cards):
        self.player_number = player_number
        self.cards = cards

    def __repr__(self):
        return "%s: %s" % (self.player_number, self.cards)

    def set_points(self, points):
        self.points = points
