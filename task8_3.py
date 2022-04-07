from functools import wraps


def type_logger(func, *args):
    @wraps(func)
    def wrapper(*args):
        print(*args, *(type(arg) for arg in args), sep=', ')
        cube = func(*args)
        return cube
    return wrapper


@type_logger
def calc_cube(*args):
    print(*(arg ** 3 for arg in args))


calc_cube(200, 3, 0, 35, 12, 1458)
