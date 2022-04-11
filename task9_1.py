from time import sleep


class TrafficLight:
    def __init__(self, color):
        self.color = color

    def running(self, sec):
        print(self.color)
        sleep(sec)


red = TrafficLight('красный')
yellow = TrafficLight('желтый')
green = TrafficLight('зеленый')
red.running(7)
yellow.running(2)
green.running(3)
