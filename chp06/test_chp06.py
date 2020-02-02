
from operator import methodcaller


upper = methodcaller('upper')
lower = methodcaller('lower')
hyphenate = methodcaller('replace', ' ', '-')


def text_preparation(text, modifier):
    return modifier(text)


def test_strategy_pattern_with_functions():
    assert text_preparation('Hello, World!', upper) == 'HELLO, WORLD!'
    assert text_preparation('Hello, World!', lower) == 'hello, world!'
    assert text_preparation('Hello, World!', hyphenate) == 'Hello,-World!'
