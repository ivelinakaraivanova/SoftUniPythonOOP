from .extended_list import IntegerList
import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self):
        self.list = IntegerList([])

    def test_add(self):
        self.assertEqual(self.list.add(25), [25])

    def test_add_raises_value_error(self):
        self.assertRaises(ValueError, self.list.add, 'text')

    def test_remove_by_index(self):
        self.list.add(30)
        element_to_remove = self.list.remove_index(0)
        self.assertEqual(element_to_remove, 30)

    def test_remove_by_index_raises_index_error(self):
        self.assertRaises(IndexError, self.list.remove_index, 3)

    def test_init_takes_integers(self):
        the_list = IntegerList('text', 28, 23.4, (2, 3), 'window')
        self.assertEqual(the_list.get_data(), [28])

    def test_get_returns_element(self):
        self.list.add(15)
        self.assertEqual(self.list.get(0), 15)

    def test_get_raises_index_error(self):
        self.assertRaises(IndexError, self.list.get, 3)

    def test_insert_raises_index_error(self):
        self.assertRaises(IndexError, self.list.insert, 2, 7)

    def test_insert(self):
        self.list.add(4)
        self.list.insert(0, 25)
        self.assertEqual(self.list.get_data(), [25, 4])

    def test_insert_raises_value_error(self):
        self.list.add(4)
        self.list.add(87)
        self.assertRaises(ValueError, self.list.insert, 0, 34.6)

    def test_get_biggest(self):
        self.list.add(4)
        self.list.add(87)
        self.assertEqual(self.list.get_biggest(), 87)

    def test_get_index(self):
        self.list.add(4)
        self.list.add(87)
        self.assertEqual(self.list.get_index(4), 0)


if __name__ == '__main__':
    unittest.main()