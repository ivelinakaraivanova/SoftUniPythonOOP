from test_cat_02.project.cat import Cat
import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('Nomi')

    def test_cat_size_is_increased_after_eating(self):
        old_size = self.cat.size
        self.cat.eat()
        self.assertEqual(self.cat.size - old_size, 1)

    def test_cat_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_raised_exception_cannot_eat_after_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as exc:
            self.cat.eat()
        self.assertEqual(str(exc.exception), 'Already fed.')

    def test_cat_raised_exception_cannot_sleep_if_hungry(self):
        with self.assertRaises(Exception) as exc:
            self.cat.sleep()
        self.assertEqual(str(exc.exception), 'Cannot sleep while hungry')

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
