import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def setUp(self):
        self.beginner = Beginner("Bina")

    def test_init(self):
        self.assertEqual(self.beginner.username, 'Bina')
        self.assertEqual(self.beginner.health, 50)
        self.assertFalse(self.beginner.is_dead)

    def test_advanced_username_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.beginner.username = ""

    def test_advanced_health_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.beginner.health = -10

    def test_advanced_is_dead_raises_error(self):
        self.assertFalse(self.beginner.is_dead)
        self.beginner.health = 0
        self.assertTrue(self.beginner.is_dead)

    def test_advanced_take_damage_raises_error(self):
        with self.assertRaises(ValueError):
            self.beginner.take_damage(-10)

    def test_advanced_take_damage(self):
        self.beginner.take_damage(10)
        self.assertEqual(self.beginner.health, 40)


# if __name__ == '__main__':
#     unittest.main()