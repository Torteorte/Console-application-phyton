from constants.constants import non_number_names_in_durak


class Card:
    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def __repr__(self):
        return "%s: %s" % (self.suit, self.name)


class CardForDurak(Card):
    text_of_class = '123'

    def __init__(self, suit, name):
        super().__init__(suit, name)

        self.nominal = None
        self.calc_nominal()

    def calc_nominal(self):
        nominal = non_number_names_in_durak.get(self.name)

        if nominal is None:
            nominal = int(self.name)

        self.nominal = nominal

    def update_nominal_by_trump(self, trump):
        if trump == self.suit:
            self.nominal += 9

    def __add__(self, other_nominal):
        if isinstance(other_nominal, CardForDurak):
            return self.nominal + other_nominal.nominal

        else:
            return self.nominal + other_nominal

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
