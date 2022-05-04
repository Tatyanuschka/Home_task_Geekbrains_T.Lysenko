class NotIntErr(Exception):
    pass


def create_ints():
    cycle_count = True
    int_lst = []
    while cycle_count:
        try:
            num = input('Введите число (для остановки введите "stop"): ')
            if not num.isdigit() and num != 'stop':
                raise NotIntErr('Это не ЧИСЛО!')
        except NotIntErr as err:
            print(err, 'Попробуйте еще раз!')
            continue
        else:
            if num == 'stop':
                break
            int_lst.append(int(num))
    return int_lst


print(create_ints())
