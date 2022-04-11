class Cloth:

    def __init__(self):
        pass

    def __str__(self):
        return f'You need {self.fabric_amount:.2f} metres of fabric to make the {self.__class__.__name__} '

    def __add__(self, other):
        return f'To make the {self.__class__.__name__} and {other.__class__.__name__}' \
               f' You need {(self.fabric_amount + other.fabric_amount):.2f} metres of fabric'

    def fabric_amount(self):
        raise NotImplementedError(self.__class__.__name__)


class Coat(Cloth):

    def __init__(self, v):
        super().__init__()
        self._v = float(v)

    @property
    def fabric_amount(self):
        return self._v / 6.5 + 0.5


class Suit(Cloth):
    def __init__(self, h):
        super().__init__()
        self._h = float(h)

    @property
    def fabric_amount(self):
        return 2 * self._h + 0.3


coat = Coat(48)
suit = Suit(1.8)
print(coat)
print(suit)
print(coat + suit)
