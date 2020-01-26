import pytest


class MyClass:
    pass


def test_hashables():
    hash(42)
    hash("hello")
    hash(('alice', 26))
    hash(frozenset([1, 2, 3, 2, 1]))
    hash(MyClass)
    hash(MyClass())

    with pytest.raises(TypeError):
        hash({1, 2, 3})


def test_dict_setdefault():
    import re

    WORD_RE = re.compile(r'\w+')

    indexes = {}

    with open('test_chp03.py') as f:
        for line_number, line in enumerate(f, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_number = match.start() + 1
                location = (line_number, column_number)
                indexes.setdefault(word, []).append(location)

    assert (25, 5) in indexes['indexes']


class MyDict(dict):

    def __missing__(self, key):
        if key < min(self.keys()):
            raise KeyError(key)
        return self[key - 1]


def test_dict_missing():
    x = MyDict([(1, 'first'), (5, 'foo'), (42, 'bar')])

    assert x[1] == 'first'
    assert x[2] == 'first'

    with pytest.raises(KeyError):
        x[0]


def test_mapping_proxy():
    from collections import Counter
    from types import MappingProxyType

    data = Counter('hello world')
    assert data['l'] == 3

    proxy = MappingProxyType(data)
    assert proxy['l'] == 3

    with pytest.raises(TypeError):
        proxy['x'] = 0

    data['x'] = 0
    assert proxy['x'] == 0
