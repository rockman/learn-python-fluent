
import math
import array
import reprlib
import operator
import functools


class Vector:
    typecode = 'd'
    shortcut_names = 'xyzy'

    def __init__(self, values):
        self._values = array.array(self.typecode, values)

    def __iter__(self):
        return iter(self._values)

    def __len__(self):
        return len(self._values)

    def __repr__(self):
        class_name = type(self).__name__
        parts = reprlib.repr(self._values)
        return '{}({})'.format(class_name, parts[parts.index('['):-1])

    def __str__(self):
        return str(tuple(self))

    def __abs__(self):
        return math.sqrt(sum(i ** 2 for i in self))

    def __bool__(self):
        return bool(abs(self))

    def __getitem__(self, index):
        part = self._values[index]
        if isinstance(index, slice):
            return Vector(part)
        return part

    def __getattr__(self, attr):
        cls = type(self)
        if len(attr) == 1:
            pos = cls.shortcut_names.find(attr)
            if 0 <= pos < len(self):
                return self[pos]
        raise AttributeError(f'{cls.__name__} has no attribute named {attr}')

    def __setattr__(self, attr, value):
        cls = type(self)
        if len(attr) == 1 and attr in cls.shortcut_names:
            raise AttributeError(f'{cls.__name__} readonly attribute {attr}')
        super().__setattr__(attr, value)

    def __eq__(self, other):
        return len(self) == len(other) and \
            all(a == b for a, b in zip(self, other))

    def __hash__(self):
        parts = (hash(i) for i in self)
        return functools.reduce(operator.xor, parts, 0)
