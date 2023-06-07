from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Billy", "dog", "woof")

    def test__init_expec_correct_values(self):
        self.assertEqual("Billy", self.mammal.name)
        self.assertEqual("dog", self.mammal.type)
        self.assertEqual("woof", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test__make_sound_expect_correct_sound(self):
        expected_value = f"{self.mammal.name} makes {self.mammal.sound}"
        actual_value = self.mammal.make_sound()
        self.assertEqual(expected_value, actual_value)

    def test__get_kingdom_expect_correct_value(self):
        expected_value = "animals"
        actual_value = self.mammal.get_kingdom()
        self.assertEqual(expected_value, actual_value)

    def test__info_expect_correct_value(self):
        expected_value = f"{self.mammal.name} is of type {self.mammal.type}"
        actual_value = self.mammal.info()
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    main()
