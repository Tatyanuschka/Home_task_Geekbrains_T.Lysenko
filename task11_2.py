class ZeroDivision(Exception):
    pass

try:
    div = int(input('Введите делитель: '))
    sep = int(input('Введите делимое: '))
    if sep == 0:
        raise ZeroDivision('На ноль делить НЕЛЬЗЯ!!!')
except ZeroDivision as e:
    print(e)
else:
    print(f'Результат деления = {div/sep:.02f}')
