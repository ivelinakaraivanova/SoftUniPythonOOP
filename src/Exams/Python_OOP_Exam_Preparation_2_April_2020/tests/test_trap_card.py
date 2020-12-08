import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def setUp(self):
        self.trap_card = TrapCard("Tripio")

    def test_init(self):
        self.assertEqual(self.trap_card.name, 'Tripio')
        self.assertEqual(self.trap_card.damage_points, 120)
        self.assertEqual(self.trap_card.health_points, 5)

    def test_trap_card_name_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.trap_card.name = ""

    def test_trap_card_health_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.trap_card.health_points = -10

    def test_t_c_health_raises_error(self):
        with self.assertRaises(ValueError) as er:
            self.trap_card.health_points = -10
        self.assertEqual(str(er.exception), "Card's HP cannot be less than zero.")

    def test_trap_card_damage_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.trap_card.health_points = -10

    def test_t_c_damage_raises_error(self):
        with self.assertRaises(ValueError) as er:
            self.trap_card.damage_points = -10
        self.assertEqual(str(er.exception), "Card's damage points cannot be less than zero.")