import unittest

from project.survivor import Survivor


class TestsSurvivor(unittest.TestCase):
    def setUp(self):
        self.survivor = Survivor('Lili', 32)

    def test_init(self):
        self.assertEqual(self.survivor.name, 'Lili')
        self.assertEqual(self.survivor.age, 32)
        self.assertEqual(self.survivor.health, 100)
        self.assertEqual(self.survivor.needs, 100)

    def test_survivor_name_raises_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.survivor.name = ""
        self.assertEqual(str(err.exception), "Name not valid!")

    def test_survivor_name(self):
        self.survivor.name = 'Ina'
        self.assertEqual(self.survivor.name, 'Ina')

    def test_survivor_age_raises_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.survivor.age = -10
        self.assertEqual(str(err.exception), "Age not valid!")

    def test_survivor_age(self):
        self.survivor.age = 28
        self.assertEqual(self.survivor.age, 28)

    def test_survivor_health_raises_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.survivor.health = -10
        self.assertEqual(str(err.exception), "Health not valid!")

    def test_survivor_health_max_100(self):
        self.survivor.health = 120
        self.assertEqual(self.survivor.health, 100)

    def test_survivor_health(self):
        self.survivor.health = 80
        self.assertEqual(self.survivor.health, 80)

    def test_survivor_needs_raises_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.survivor.needs = -10
        self.assertEqual(str(err.exception), "Needs not valid!")

    def test_survivor_needs_max_100(self):
        self.survivor.needs = 120
        self.assertEqual(self.survivor.needs, 100)

    def test_survivor_needs(self):
        self.survivor.needs = 80
        self.assertEqual(self.survivor.needs, 80)

    def test_survivor_needs_sustenance(self):
        self.assertFalse(self.survivor.needs_sustenance)
        self.survivor.needs -= 20
        self.assertTrue(self.survivor.needs_sustenance)

    def test_survivor_needs_healing(self):
        self.assertFalse(self.survivor.needs_healing)
        self.survivor.health -= 20
        self.assertTrue(self.survivor.needs_healing)
