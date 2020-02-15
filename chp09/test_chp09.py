from vector2d import Vector2d
import pytest


SAMPLE_BYTES = b"d\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@"


def test_repr_and_str():
    v = Vector2d(3, 4)

    assert repr(v) == "Vector2d(3.0, 4.0)"
    assert str(v) == "(3.0, 4.0)"


def test_equality():
    a = Vector2d(3, 4)
    b = Vector2d(3, 4)

    assert a == b


def test_abs():
    a = Vector2d(3, 4)

    assert abs(a) == 5


def test_bool():
    assert bool(Vector2d(3, 4))
    assert bool(Vector2d(0, 4))
    assert bool(Vector2d(3, 0))
    assert not bool(Vector2d(0, 0))


def test_unpacking():
    a = Vector2d(3, 4)
    x, y = a

    assert x == 3.0
    assert y == 4.0


def test_bytes():
    a = Vector2d(3, 4)

    assert bytes(a) == SAMPLE_BYTES


def test_frombytes():
    a = Vector2d.frombytes(SAMPLE_BYTES)

    assert a == Vector2d(3, 4)


def test_format():
    a = Vector2d(3, 4)

    assert "{:.1f}".format(a) == "(3.0, 4.0)"
    assert "{:.2f}".format(a) == "(3.00, 4.00)"
    assert "{:.1fp}".format(a) == "<5.0, 0.9>"


def test_immutable():
    a = Vector2d(3, 4)

    with pytest.raises(AttributeError):
        a.x = 0


def test_hashable():
    a = Vector2d(3, 4)

    assert hash(a) == 7
    assert set([a])  # expect no exception thrown
