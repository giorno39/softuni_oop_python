import sys
from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 50)
        self.vehicle.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def test__init_expect_correct_value(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(50, self.vehicle.horse_power)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test__drive__when_not_enough_fuel_expect_raise(self):
        kilometers = sys.maxsize
        with self.assertRaises(Exception) as error:
            self.vehicle.drive(kilometers)

        self.assertIsNotNone(error)
        self.assertEqual("Not enough fuel", str(error.exception))

    def test__drive_when_enough_fuel_expect_fuel_to_decrease(self):
        self.vehicle.drive(20)
        expected_value = 75
        self.assertEqual(expected_value, self.vehicle.fuel)

    def test__refuel_when_fuel_exceeds_capacity(self):
        capacity = self.vehicle.capacity
        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(capacity + 1)

        self.assertIsNotNone(error)
        self.assertEqual("Too much fuel", str(error.exception))

    def test_refuel_when_there_is_enough_space(self):
        self.vehicle.fuel -= 20
        self.vehicle.refuel(20)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)

    def test__str__test_string_representation(self):
        expected_value = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"

        actual_value = self.vehicle.__str__()

        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    main()
