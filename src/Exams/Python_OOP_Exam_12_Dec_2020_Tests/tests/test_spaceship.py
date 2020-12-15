import unittest

from project.spaceship.spaceship import Spaceship


class TestsSpaceship(unittest.TestCase):
    def setUp(self):
        self.spaceship = Spaceship("SpaceX", 3)

    def test_init(self):
        self.assertEqual(self.spaceship.name, "SpaceX")
        self.assertEqual(self.spaceship.capacity, 3)
        self.assertEqual(self.spaceship.astronauts, [])

    def test_add_astronaut_append(self):
        self.spaceship.add("John")
        self.spaceship.add("Michael")
        self.spaceship.add("Tom")
        self.assertEqual(self.spaceship.astronauts, ["John", "Michael", "Tom"])

    def test_add_raises_value_error(self):
        self.spaceship.add("John")
        self.spaceship.add("Michael")
        self.spaceship.add("Tom")
        with self.assertRaises(ValueError) as err:
            self.spaceship.add("Peter")
        self.assertEqual(str(err.exception), "Spaceship is full")

    def test_add_astronaut_already_in(self):
        self.spaceship.add("John")
        self.spaceship.add("Michael")
        with self.assertRaises(ValueError) as err:
            self.spaceship.add("John")
        self.assertEqual(str(err.exception), "Astronaut John Exists")

    def test_add_format(self):
        result = self.spaceship.add("John")
        self.assertEqual(result, "Added astronaut John")

    def test_remove(self):
        self.spaceship.add("John")
        self.spaceship.add("Michael")
        with self.assertRaises(ValueError) as err:
            self.spaceship.remove("Tom")
        self.assertEqual(str(err.exception), "Astronaut Not Found")

    def test_remove_format(self):
        self.spaceship.add("John")
        result = self.spaceship.remove("John")
        self.assertEqual(result, "Removed John")
