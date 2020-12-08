import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def setUp(self):
        self.card_rep = CardRepository()

    def test_init(self):
        self.assertEqual(self.card_rep.count, 0)
        self.assertEqual(self.card_rep.cards, [])

    def test_add_card_raises_value_error(self):
        magic_card = MagicCard("Magi")
        self.card_rep.add(magic_card)
        with self.assertRaises(ValueError) as err:
            self.card_rep.add(magic_card)
        self.assertEqual(str(err.exception), "Card Magi already exists!")

    def test_add_card(self):
        magic_card = MagicCard("Magi")
        self.card_rep.add(magic_card)
        self.assertEqual(self.card_rep.cards, [magic_card])

    def test_add_card_count(self):
        magic_card = MagicCard("Magi")
        self.card_rep.add(magic_card)
        self.assertEqual(self.card_rep.count, 1)

    def test_remove_card_raises_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.card_rep.remove("")
        self.assertEqual(str(err.exception), "Card cannot be an empty string!")

    def test_remove_card(self):
        magic_card = MagicCard("Magi")
        self.card_rep.add(magic_card)
        self.card_rep.remove("Magi")
        self.assertEqual(self.card_rep.cards, [])

    def test_remove_card_count(self):
        magic_card = MagicCard("Magi")
        self.card_rep.add(magic_card)
        self.card_rep.remove("Magi")
        self.assertEqual(self.card_rep.count, 0)

    def test_find_card(self):
        magic_card = MagicCard("Magi")
        self.card_rep.add(magic_card)
        self.assertEqual(self.card_rep.find("Magi"), magic_card)