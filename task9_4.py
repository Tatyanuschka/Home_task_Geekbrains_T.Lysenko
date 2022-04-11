class Car:

    def __init__(self, name, color, speed, ispolice = False):
        self.name = name
        self.color = color
        self.speed = speed
        self.ispolice = ispolice

    def go(self):
        print(f'{self.name} поехала со скоростью {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'{self.name} останавилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} = {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превысила скорость, Ваша скорость - {self.speed}')
        else:
            print(f'Скорость {self.name} = {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превысила скорость, Ваша скорость - {self.speed}')
        else:
            print(f'Скорость {self.name} = {self.speed}')

class PoliceCar(Car):

    def __init__(self, name, color, speed, ispolice = True):
        super().__init__(name, color, speed, ispolice=False)
        self.ispolice = True


auto_town = TownCar('Mazda', 'белая', 200)
auto_work = WorkCar('Largus', 'серый', 80)
auto_sport = SportCar('Jaguar', 'red', 250)
auto_police = PoliceCar('BMW', 'blue', 120)
auto_town.go()
auto_work.stop()
auto_sport.go()
auto_police.turn('налево')
auto_town.show_speed()
auto_work.show_speed()
auto_police.show_speed()