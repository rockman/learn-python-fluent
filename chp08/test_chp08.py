
import weakref


def test_equals_vs_identity():

    class Foo:
        def __eq__(self, other):
            return False

    a = Foo()
    b = a

    assert a is b
    assert a != b


def test_shallow_copy():
    a = [1, ['hello', 'world'], (3.0,  4.0)]
    b = list(a)

    assert a == b
    assert a is not b

    a[1].append('!')

    assert a == b

    b[-1] += (5.0, 6.0)

    assert a != b


def test_deep_copy():
    import copy

    class Container:
        def __init__(self, values):
            self.values = list(values)

        def __eq__(self, other):
            return self.values == other.values

    a = Container([1, 2, 3])
    b = copy.copy(a)
    c = copy.deepcopy(a)

    assert a == b
    assert a == c

    a.values.append(4)

    assert a == b
    assert a != c


def test_weakref_finalize():
    a = {1, 2, 3}
    b = a
    counter = 0

    def bye():
        nonlocal counter
        counter += 1

    f = weakref.finalize(a, bye)

    assert f.alive

    del a

    assert f.alive
    assert counter == 0

    b = 'something else'

    assert not f.alive
    assert counter == 1


def test_weakref():
    a = {1, 2, 3}
    wref = weakref.ref(a)

    assert a == wref()

    a = 'something else'

    assert wref() is None


def test_weakvaluedictionary():

    class Blob:
        def __init__(self, value):
            self.value = value

    wvd = weakref.WeakValueDictionary()

    data = [
        ('a', Blob('hello')),
        ('b', Blob(42)),
        ('c', Blob({0, 1})),
    ]

    for key, value in data:
        wvd[key] = value

    assert len(wvd) == 3

    del data[1]

    assert len(wvd) == 2

    data = 'something else'

    assert len(wvd) == 1
    assert 'c' in wvd

    del value

    assert len(wvd) == 0


def test_tuple_copy_returns_same_tuple():
    a = (1, 2, 3)
    b = a[:]

    assert a is b


def test_string_interning():
    a = 'hello'
    b = 'hello'

    assert a is b
