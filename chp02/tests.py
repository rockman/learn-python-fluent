
import array
import unittest
import collections


class Chp02Tests(unittest.TestCase):

    def test_cartesian_product(self):
        colors = 'black white'.split()
        sizes = list('SML')
        shirts = [(c, s) for c in colors for s in sizes]
        self.assertEqual(shirts[1], ('black', 'M'))

    def test_tuple_from_generator(self):
        t = tuple(i * 2 for i in range(1, 4))
        self.assertEqual(t, (2, 4, 6))

    def test_array_from_generator(self):
        a = array.array('b', (ord(c) for c in 'hello, world'))
        self.assertEqual(a[6], 32)

    def test_tuple_unpacking(self):
        a, b, c = ('hello', 42, lambda x: -x)
        self.assertEqual(a, 'hello')
        self.assertEqual(b, 42)
        self.assertEqual(c(1), -1)

        t = (7, 2)
        q, r = divmod(*t)
        self.assertEqual(q, 3)
        self.assertEqual(r, 1)

        a, b, *c = range(5)
        self.assertEqual(a, 0)
        self.assertEqual(b, 1)
        self.assertEqual(c, [2, 3, 4])

        a, *b, c = range(5)
        self.assertEqual(a, 0)
        self.assertEqual(b, [1, 2, 3])
        self.assertEqual(c, 4)

        *a, b, c = range(5)
        self.assertEqual(a, [0, 1, 2])
        self.assertEqual(b, 3)
        self.assertEqual(c, 4)

    def test_nested_tuple_unpacking(self):
        items = [
            ('alpha', (1, 2)),
            ('beta', (3, 4)),
            ('gamma', (5, 6)),
        ]

        self.assertEqual([x + y for _, (x, y) in items], [3, 7, 11])

    def test_namedtuple(self):
        Item = collections.namedtuple('Item', ['name', 'coords'])
        a = Item('alpha', (1, 2))

        values = ('beta', (3, 4))
        b = Item._make(values)

        c = Item(coords=(5, 6), name='gamma')

        self.assertEqual(a.name, 'alpha')
        self.assertEqual(b.coords[0], 3)
        self.assertEqual(c, Item('gamma', (5, 6)))

        items = [a, b, c]
        self.assertEqual([sum(coords) for _, coords in items], [3, 7, 11])

    def test_slices(self):
        values = list('python')
        self.assertEqual(values[1:], list('ython'))
        self.assertEqual(values[:-1], list('pytho'))
        self.assertEqual(values[::2], list('pto'))

        s = slice(1, -1, 2)
        self.assertEqual(values[s], list('yh'))

        values[2:-1] = list('xyz')
        self.assertEqual(values, list('pyxyzn'))

    def test_building_lists(self):
        a5 = 'a' * 5
        self.assertEqual(a5, 'aaaaa')

        xyz3 = 3 * 'xyz'
        self.assertEqual(xyz3, 'xyzxyzxyz')

        items = ['a', 42, (3, 4)] * 2
        self.assertEqual(items, ['a', 42, (3, 4), 'a', 42, (3, 4)])

        bad_list_of_lists = [list('_') * 3] * 2
        bad_list_of_lists[0][0] = 'X'
        self.assertEqual(bad_list_of_lists[1][0], 'X')

        good_list_of_lists = [list('_') * 3 for i in range(2)]
        good_list_of_lists[0][0] = 'X'
        self.assertEqual(good_list_of_lists[1][0], '_')
