from .car_manager import Car
import unittest


class CarManagerTests(unittest.TestCase):
    def setUp(self):
        self.car = Car('ford', 'fiesta', 3, 10)

    def test_init(self):
        self.assertEqual(self.car.make, 'ford')
        self.assertEqual(self.car.model, 'fiesta')
        self.assertEqual(self.car.fuel_consumption, 3)
        self.assertEqual(self.car.fuel_capacity, 10)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_empty_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.make = ''

    def test_model_empty_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.model = ''

    def test_fuel_consumption_negative_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = -3

    def test_fuel_capacity_negative_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = 0

    def test_refuel_negative_raises_exception(self):
        self.assertRaises(Exception, self.car.refuel, -2)

    def test_refuel(self):
        self.car.refuel(2)
        self.assertEqual(self.car.fuel_amount, 2)

    def test_refuel_more_than_capacity(self):
        self.car.refuel(12)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_needed_more_than_fuel_amount(self):
        self.assertRaises(Exception, self.car.drive, 200)

    def test_fuel_amount(self):
        self.car.refuel(5)
        self.car.drive(50)
        self.assertEqual(self.car.fuel_amount, 3.5)


if __name__ == '__main__':
    unittest.main()