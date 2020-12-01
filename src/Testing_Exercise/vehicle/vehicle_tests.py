from .vehicle_project import Car, Truck
import unittest


class CarTests(unittest.TestCase):
    def setUp(self):
        self.car = Car(40, 5)

    def test_init(self):
        self.assertEqual(self.car.fuel_quantity, 40)
        self.assertEqual(self.car.fuel_consumption, 5)

    def test_drive_not_enough_fuel(self):
        self.car.drive(50)
        self.assertEqual(self.car.fuel_quantity, 40)

    def test_drive_enough_fuel(self):
        self.car.drive(2)
        self.assertEqual(self.car.fuel_quantity, 28.2)

    def test_refuel(self):
        self.car.refuel(15)
        self.assertEqual(self.car.fuel_quantity, 55)


class TruckTests(unittest.TestCase):
    def setUp(self):
        self.truck = Truck(100, 15)

    def test_init(self):
        self.assertEqual(self.truck.fuel_quantity, 100)
        self.assertEqual(self.truck.fuel_consumption, 15)

    def test_drive_not_enough_fuel(self):
        self.truck.drive(20)
        self.assertEqual(self.truck.fuel_quantity, 100)

    def test_drive_enough_fuel(self):
        self.truck.drive(5)
        self.assertEqual(self.truck.fuel_quantity, 17)

    def test_refuel(self):
        self.truck.refuel(40)
        self.assertEqual(self.truck.fuel_quantity, 138)


if __name__ == '__main__':
    unittest.main()