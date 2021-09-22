def type_logger(func):
    def wrapper(*args):
        calc = func(*args)
        for el in args:
            print(f'{el}: {type(el)}')
        return calc

    return wrapper


@type_logger
def calc_cube(x, *args):
    return x ** 3


a = calc_cube(3, 5, 7, 9)
print(a)
