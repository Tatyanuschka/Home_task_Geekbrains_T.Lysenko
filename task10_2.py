from abc import ABC, abstractmethod

class Cloth(ABC):
    expense_count = 0


    @abstractmethod
    def expense(self):
        pass


class Coat(Cloth):

    def __init__(self, v):
        self.v = v
        Coat.expense_count += self.expense


    def __str__(self):
        return f'Для пальто размером {self.v} требуется ткань в кол-ве {self.expense}, общий расход = {Coat.expense_count:.02f}'


    @property
    def expense(self):
        return float(self.v / 6.5 + 0.5)


class Suit(Cloth):
    def __init__(self, h):
        self.h = h
        Suit.expense_count += self.expense


    def __str__(self):
        return f'Для костюма размером {self.h} требуется ткань в кол-ве {self.expense}, общий расход = {Suit.expense_count:.02f}'


    @property
    def expense(self):
        return float(2 * self.h + 0.3)


coat = Coat(48)
suit = Suit(1.8)
print(coat)
print(suit)
coat2 = Coat(56)
suit2 = Suit(1.6)
print(coat2)
print(suit2)

