from labs.cat import Cat

import unittest
from unittest import TestCase


class CatTest(TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Suzi")

    def test__eat_when_is_hungry(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertEqual(1, self.cat.size)

    def test__eat_when_fed_expect_raise(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as error:
            self.cat.eat()

        self.assertIsNotNone(error)
        self.assertEqual('Already fed.', str(error.exception))

    def test__sleep_when_not_fed_expect_raise(self):
        with self.assertRaises(Exception) as error:
            self.cat.sleep()

        self.assertIsNotNone(error)

    def test__sleep_expect_to_sleep(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()

