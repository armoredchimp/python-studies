def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)

    # print(kwargs['add'])
    n += kwargs['add']
    n *= kwargs['multiply']


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get['make']
        self.model = kw.get['model']


my_car = Car(make='Toyota', model='Camry')
