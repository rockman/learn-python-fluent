
import random
import unittest

import cards
import vector


class CardsTests(unittest.TestCase):

    def setUp(self):
        self.deck = cards.Deck()

    def test_len(self):
        self.assertEqual(52, len(self.deck))

    def test_indexing(self):
        self.verify_card(self.deck[0], '2', 'spades')
        self.verify_card(self.deck[-1], 'A', 'hearts')

    def test_slicing(self):
        x = self.deck[:3]
        self.verify_card(x[0], '2', 'spades')
        self.verify_card(x[1], '3', 'spades')
        self.verify_card(x[2], '4', 'spades')

    def test_choice(self):
        print(random.choice(self.deck))

    def test_iterate(self):
        for card in self.deck:
            print(card)
        self.verify_card(card, 'A', 'hearts')

    def test_iterate_reversed(self):
        for card in reversed(self.deck):
            print(card)
        self.verify_card(card, '2', 'spades')

    def test_contains(self):
        self.assertTrue(cards.Card('K', 'clubs') in self.deck)

    def verify_card(self, card, rank, suit):
        self.assertEqual(card.rank, rank)
        self.assertEqual(card.suit, suit)


class VectorTests(unittest.TestCase):

    def setUp(self):
        self.a = vector.Vector(1, 2)
        self.b = vector.Vector(3, 4)

    def test_repr(self):
        self.assertEqual('Vector(1, 2)', repr(self.a))

    def test_bool(self):
        self.assertTrue(self.a)
        self.assertTrue(self.b)
        self.assertTrue(vector.Vector(0, 1))
        self.assertTrue(vector.Vector(1, 0))
        self.assertFalse(vector.Vector(0, 0))

    def test_add(self):
        self.verify_vector(self.a + self.b, 4, 6)

    def test_sub(self):
        self.verify_vector(self.a - self.b, -2, -2)

    def test_mul(self):
        self.verify_vector(self.a * 2, 2, 4)

    def test_div(self):
        self.verify_vector(self.b / 2, 1.5, 2)

    def test_hypot(self):
        self.assertAlmostEqual(5, abs(vector.Vector(3, 4)))

    def verify_vector(self, vector, x, y):
        self.assertEqual(vector.x, x)
        self.assertEqual(vector.y, y)
