class Player:
    def __init__(self, player_number):
        self.player_number = player_number
        self.cards = []
        self.points = 0

    def add_card(self, card):
        self.cards.append(card)

    def __repr__(self):
        return "%s: %s" % (self.player_number, self.cards)

    def calc_points(self):
        self.points = sum(self.cards)
