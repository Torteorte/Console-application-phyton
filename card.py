class Card:
    nominal = 0

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def __repr__(self):
        return "%s: %s" % (self.name, self.suit)

    def set_nominal(self, trump, nominal):
        if trump == self.suit:
            self.nominal = nominal + 9
        else:
            self.nominal = nominal
