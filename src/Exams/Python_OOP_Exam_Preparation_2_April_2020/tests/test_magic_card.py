import unittest
from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def setUp(self):
        self.magic_card = MagicCard("Trio")

    def test_init(self):
        self.assertEqual(self.magic_card.name, 'Trio')
        self.assertEqual(self.magic_card.damage_points, 5)
        self.assertEqual(self.magic_card.health_points, 80)

    def test_magic_card_name_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.magic_card.name = ""

    def test_magic_card_health_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.magic_card.health_points = -10

    def test_m_c_health_raises_error(self):
        with self.assertRaises(ValueError) as er:
            self.magic_card.health_points = -10
        self.assertEqual(str(er.exception), "Card's HP cannot be less than zero.")

    def test_magic_card_damage_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.magic_card.health_points = -10

    def test_m_c_damage_raises_error(self):
        with self.assertRaises(ValueError) as er:
            self.magic_card.damage_points = -10
        self.assertEqual(str(er.exception), "Card's damage points cannot be less than zero.")
