import unittest

from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room('Johanson', 100, 2)

    def test_init(self):
        self.assertEqual(self.room.family_name, 'Johanson')
        self.assertEqual(self.room.budget, 100)
        self.assertEqual(self.room.members_count, 2)
        self.assertEqual(self.room.children, [])
        self.assertEqual(self.room.expenses, 0)

    def test_room_expenses_raises_value_error(self):
        with self.assertRaises(ValueError) as err:
            self.room.expenses = -10
        self.assertEqual(str(err.exception), "Expenses cannot be negative")
