from test_worker_01.project.worker import Worker
import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Ivan', 1000, 50)

    def test_worker_is_initialized_correctly(self):
        self.assertEqual(self.worker.name, 'Ivan')
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 50)

    def test_energy_is_increased_after_rest(self):
        old_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy - old_energy, 1)

    def test_worker_raised_exception_if_tries_work_with_negative_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()
        self.worker.energy = -5
        with self.assertRaises(Exception):
            self.worker.work()

    def test_money_is_increased_by_salary_after_work(self):
        old_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money - old_money, self.worker.salary)

    def test_worker_energy_is_decreased_after_work(self):
        old_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(self.worker.energy - old_energy, -1)

    def test_get_info(self):
        info = self.worker.get_info()
        self.assertEqual(info, 'Ivan has saved 0 money.')


if __name__ == '__main__':
    unittest.main()
