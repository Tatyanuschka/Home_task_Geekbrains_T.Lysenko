class Cell:

    def __init__(self, amount):
        self.amount = int(amount)

    def __str__(self):
        return f'Количество клеток = {self.amount}'

    def __add__(self, other): # сложение клеток
        return f'Количество клеток после СЛОЖЕНИЯ = {Cell(self.amount + other.amount)}'

    def __sub__(self, other):  # вычитание
        if self.amount < other.amount:
            raise ValueError('Вычитание невозможно, уменьшаемое меньше вычитаемого')
        else:
            return f'Результат вычитания  = {Cell(self.amount - other.amount)} ячеек'

    def __mul__(self, other): # умножение
        return f'Результат УМНОЖЕНИЯ = {Cell(self.amount * other.amount)} ячеек'

    def __floordiv__(self, other):
        return f'Создана общая клетка из 2 путем деления, количество ячеек = {Cell(self.amount // other.amount)}'

    def make_order(self, row_amount):
        res = ''
        for i in range(self.amount // row_amount):
            res += '*' * row_amount + '\n'
        res += '*' * (self.amount % row_amount) + '\n'
        return res



cell1 = Cell(4)
cell2 = Cell(12)
print(cell1)
print(cell2)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell2 // cell1)
print(cell2.make_order(5))

