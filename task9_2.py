class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self, mass_one_meter=25, thick=5):
        return self._width * self._length * mass_one_meter * thick / 1000


road = Road(100, 20)
print(road.mass_calc())
