
from functools import singledispatch
import numbers


def averager():
    values = []

    def average(value):
        values.append(value)
        return sum(values) // len(values)

    return average


def test_closures():
    avg = averager()

    assert avg(10) == 10
    assert avg(20) == 15
    assert avg(30) == 20


def counter(f):
    count = 0

    def wrapper(n):
        nonlocal count
        count += 1
        return f(n), count

    return wrapper


def test_counter():
    @counter
    def echo(n):
        return n

    assert echo(42) == (42, 1)
    assert echo('what') == ('what', 2)


@singledispatch
def funky(obj):
    return f'object:{obj}'


@funky.register(str)
def _(s):
    return f'string:{s}'


@funky.register(numbers.Integral)
def _(n):
    return f'integral:{n}'


def test_singledispatch():
    assert funky(test_singledispatch).startswith('object:<function ')
    assert funky('hello') == 'string:hello'
    assert funky(42) == 'integral:42'


def star(n=3):
    def decorate(f):
        def wrapper():
            stars = '*' * n
            return f'{stars}:{f()}'
        return wrapper
    return decorate


def test_parameterized_decorator():
    @star()
    def hello():
        return 'hello'

    @star(1)
    def world():
        return 'world'

    assert hello() == '***:hello'
    assert world() == '*:world'
