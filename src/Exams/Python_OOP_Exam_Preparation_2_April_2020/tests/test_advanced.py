import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    def setUp(self):
        self.advanced = Advanced("Bella")

    def test_init(self):
        self.assertEqual(self.advanced.username, 'Bella')
        self.assertEqual(self.advanced.health, 250)
        self.assertFalse(self.advanced.is_dead)

    def test_advanced_username_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.advanced.username = ""

    def test_advanced_health_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.advanced.health = -10

    def test_advanced_is_dead_raises_error(self):
        self.assertFalse(self.advanced.is_dead)
        self.advanced.health = 0
        self.assertTrue(self.advanced.is_dead)

    def test_advanced_take_damage_raises_error(self):
        with self.assertRaises(ValueError):
            self.advanced.take_damage(-10)

    def test_advanced_take_damage(self):
        self.advanced.take_damage(100)
        self.assertEqual(self.advanced.health, 150)

#
# if __name__ == '__main__':
#     unittest.main()