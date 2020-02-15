import math
from array import array


class Vector2d:
    __slots__ = ("__x", "__y")

    typecode = "d"

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @classmethod
    def frombytes(cls, bs):
        typecode = chr(bs[0])
        memv = memoryview(bs[1:]).cast(typecode)
        return cls(*memv)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __repr__(self):
        cls_name = type(self).__name__
        return "{}({!r}, {!r})".format(cls_name, self.x, self.y)

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __iter__(self):
        return iter((self.x, self.y))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=""):
        if fmt_spec.endswith("p"):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = "<{}, {}>"

        else:
            coords = self
            outer_fmt = "({}, {})"

        parts = (format(i, fmt_spec) for i in coords)
        return outer_fmt.format(*parts)
