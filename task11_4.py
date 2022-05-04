class WareHouse:
    __instance = None

    def __new__(cls, *args, **kwargs):  #метод, который не позволяет создать более 1 экз класса
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.wh_dict = {}

    def __str__(self):  # метод выводит в консоль данные по складу
        res = ''
        for key in self.wh_dict:
            res += key + '\n'
            for item in self.wh_dict[key]:
                res += item['name'] + ' ' + str(item['amount']) + '\n'
            res += '*' * 10 + '\n'
        return res

    def __del__(self):                  #Если экземпляр класса будет удален сборщиком мусора
        WareHouse.__instance = None


class HardWare:
    """родительский класс для оргтехники"""
    hw_dict = {}
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    @classmethod
    def cls_name(cls):
        return cls.__name__

    @staticmethod
    def validation_amount(num):
        if type(num) != int or num <= 0:
            raise TypeError ('количеством должно быть целым положительным числом!')
        else:
            return num

    def add_to_wh(self, amount):
        """метод добавляет в объект склада аттрибуты объекта оргтехники"""
        available_count = False
        if self.cls_name() not in wh.wh_dict:
            self.__dict__['amount'] = self.validation_amount(amount)
            wh.wh_dict[self.cls_name()] = [(self.__dict__)]
        else:
            for prod in wh.wh_dict[self.cls_name()]:
                if prod['name'] == self.name:
                    prod['amount'] += self.validation_amount(amount)
                    available_count = True
                    break
                else:
                    available_count = False
                    continue
            if not available_count:
                self.__dict__['amount'] = self.validation_amount(amount)
                wh.wh_dict[self.cls_name()].append(self.__dict__)

    def de_stock(self, amount):
        """метод списания товара со склада"""
        amount = self.validation_amount(amount)
        if not self.__dict__['amount']:
            raise Exception('Такого товара на складе нет')
        if amount > self.__dict__['amount']:
            raise ValueError(f"Запрашиваемое количество больше, чем есть в наличии ({self.__dict__['amount']}")
        else:
            self.__dict__['amount'] = self.__dict__['amount'] - amount
            if self.__dict__['amount'] == 0:
                wh.wh_dict[self.cls_name()].remove(self.__dict__)


class Printer(HardWare):
    def __init__(self, name, cost, color = True):
        super().__init__(name, cost)
        self.color = color


class Monitor(HardWare):
    def __init__(self, name, cost, screensize):
        super().__init__(name, cost)
        self.screensize = screensize


class Laptop(HardWare):
    def __init__(self, name, cost, screensize, processor, work_memory):
        super().__init__(name, cost)
        self.processor = processor
        self.work_memory = work_memory
        self.screensize = screensize


class PowerSupply(HardWare):
    def __init__(self, name, cost, power):
        super().__init__(name, cost)
        self.power = power


class KeyBoard(HardWare):
    def __init__(self, name, cost, wired = True):
        super().__init__(name, cost)
        self.wired = wired


class Mouse(HardWare):
    def __init__(self, name, cost, color, wired = True):
        super().__init__(name, cost)
        self.color = color
        self.wired = wired


class WebCam(HardWare):
    def __init__(self, name, cost, resolution, wired = True):
        super().__init__(name, cost)
        self.resolution = resolution
        self.wired = wired


wh = WareHouse()  # объект склада
printer = Printer('hp', 20000)
printer.add_to_wh(1)
monitor = Monitor('Samsung', 30000, 28)
monitor.add_to_wh(1)
printer2 = Printer('LG', 15000)
printer2.add_to_wh(1)
mouse = Mouse('Logitech', 2000, 'black')
mouse.add_to_wh(1)
laptop = Laptop('Asus', 34000, 28, 'Intel Core i5', '8Gb')
laptop.add_to_wh(1)
monitor.add_to_wh(10)
laptop.add_to_wh(1)
printer.add_to_wh(2)
laptop.add_to_wh(10)
laptop2 = Laptop('MacBook', 100000, 15, 'Intel', '16Gb')
laptop2.add_to_wh(3)
laptop2.add_to_wh(10)

print(wh)
laptop2.de_stock(12)
printer.de_stock(3)
print(wh)








