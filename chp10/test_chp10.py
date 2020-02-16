
from vector import Vector
import pytest


def test_basics():
    a = Vector([3, 4])
    b = Vector([3, 4])

    assert len(a) == 2
    assert list(a) == [3.0, 4.0]
    assert repr(a) == 'Vector([3.0, 4.0])'
    assert str(a) == '(3.0, 4.0)'
    assert a == b
    assert abs(a) == 5
    assert bool(a)
    assert not bool(Vector([0]))
    assert a[1] == 4
    assert hash(a)  # can hash vector
    assert hash(Vector([])) == 0


def test_slicing():
    a = Vector(range(10))
    b = a[:5]

    assert type(b) == Vector
    assert repr(b) == 'Vector([0.0, 1.0, 2.0, 3.0, 4.0])'


def test_repr_for_large_vectors():
    a = Vector(range(100))

    assert repr(a) == 'Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])'


def test_attributes():
    a = Vector([3, 4])

    assert a.x == 3
    assert a.y == 4

    with pytest.raises(AttributeError):
        a.z

    with pytest.raises(AttributeError):
        a.x = 0

    a.q = 'setting to a non special attribute name is allowed'
