from labs.worker import Worker

import unittest
from unittest import TestCase


class TestWorker(TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Vasko", 2000, 2)

    def test__init_expect_to_initialize_worker(self):
        self.assertEqual("Vasko", self.worker.name)
        self.assertEqual(2000, self.worker.salary)
        self.assertEqual(2, self.worker.energy)

    def test__rest__expect_to_increase_energy(self):
        self.worker.rest()
        self.assertEqual(3, self.worker.energy)

    def test__work__with_0_energy_expect_raise(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as error:
            self.worker.work()

        self.assertIsNotNone(error)
        self.assertEqual("Not enough energy.", str(error.exception))

    def test__work__expect_money_to_increase_by_salary(self):
        self.worker.work()
        self.worker.work()

        self.assertEqual(2 * self.worker.salary, self.worker.money)

    def test__work__expect_energy_to_decrease(self):
        self.worker.work()
        self.worker.work()

        self.assertEqual(0, self.worker.energy)

    def test__get_info_expect_correct_information(self):
        expected_info = f'{self.worker.name} has saved {self.worker.money} money.'
        actual_info = self.worker.get_info()

        self.assertEqual(expected_info, actual_info)


if __name__ == "__main__":
    unittest.main()
