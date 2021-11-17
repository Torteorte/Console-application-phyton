from constants import non_number_names_in_durak


class Card:
    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def __repr__(self):
        return "%s: %s" % (self.name, self.suit)


class CardForDurak(Card):
    def __init__(self, suit, name):
        super().__init__(suit, name)

        self.nominal = None
        self.calc_nominal()

    def calc_nominal(self):
        nominal = non_number_names_in_durak.get(self.name)

        if nominal is None:
            nominal = int(self.name)

        self.nominal = nominal

    def set_nominal(self, trump):
        if trump == self.suit:
            self.nominal += 9
