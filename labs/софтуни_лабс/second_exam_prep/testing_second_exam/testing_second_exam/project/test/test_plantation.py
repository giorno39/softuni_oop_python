from project.plantation import Plantation
from unittest import TestCase

# from testing_second_exam.project.plantation import Plantation


class PlantationTest(TestCase):
    def test__init__expect_correct_values(self):
        plantation = Plantation(10)
        self.assertEqual(10, plantation.size)
        self.assertEqual({}, plantation.plants)
        self.assertEqual([], plantation.workers)

    def test__init_when_size_is_negative_expect_raise(self):
        with self.assertRaises(ValueError) as error:
            plantation = Plantation(-2)

        self.assertIsNotNone(error)
        self.assertEqual("Size must be positive number!", str(error.exception))

    def test__hire_worker_when_already_hired_expect_raise(self):
        plantation = Plantation(10)
        plantation.hire_worker("Vasko")
        with self.assertRaises(ValueError) as error:
            plantation.hire_worker("Vasko")

        self.assertIsNotNone(error)
        self.assertEqual("Worker already hired!", str(error.exception))

    def test__hire_worker_expect_worker_to_be_hired(self):
        plantation = Plantation(10)
        actual_result = plantation.hire_worker("Vasko")
        expected_result = f"Vasko successfully hired."
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(["Vasko"], plantation.workers)

    def test__len__func_if_calc_is_right(self):
        plantation = Plantation(10)
        plantation.plants[1] = "a"
        plantation.plants[2] = "b"
        actual_result = len(plantation)
        self.assertEqual(2, actual_result)

    def test__len__func_when_dict_is_empty(self):
        plantation = Plantation(10)
        self.assertEqual(0, len(plantation))


    def test__planting_with_an_unvalid_worker_expect_raise(self):
        plantation = Plantation(10)
        with self.assertRaises(ValueError) as error:
            plantation.planting("Vasko", "zele")

        self.assertIsNotNone(error)
        self.assertEqual("Worker with name Vasko is not hired!", str(error.exception))


    def test__planting_when_there_is_no_space_left_expect_raise(self):
        plantation = Plantation(1)
        plantation.plants[1] = "a"
        plantation.workers = ["Vasko"]

        with self.assertRaises(ValueError) as error:
            plantation.planting("Vasko", "zele")

        self.assertIsNotNone(error)
        self.assertEqual("The plantation is full!", str(error.exception))

    def test__planting_when_worker_already_planted_before(self):
        plantation = Plantation(10)
        plantation.workers.append("Vasko")
        plantation.plants["Vasko"] = ["zele"]

        actual_result = plantation.planting("Vasko", "apple")
        expected_result = "Vasko planted apple."
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({"Vasko": ["zele", "apple"]}, plantation.plants)

    def test__planting_when_worker_plants_for_the_first_time(self):
        plantation = Plantation(10)
        plantation.workers.append("a")

        actual_result = plantation.planting("a", "apple")
        expected_result = "a planted it's first apple."
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({"a": ["apple"]}, plantation.plants)

    def test__repr_expect_correct_value(self):
        plantation = Plantation(10)
        plantation.workers = ["a", "b"]
        actual_result = repr(plantation)
        expected_result = 'Size: 10\n' + f'Workers: {", ".join(plantation.workers)}'
        self.assertEqual(expected_result, actual_result)

    def test__str__expect_correct_value(self):
        plantation = Plantation(10)
        plantation.workers.append("a")
        plantation.plants["a"] = ["zele", "apple"]
        to_join = [f"Plantation size: {10}", f'{", ".join(plantation.workers)}', f"a planted: {', '.join(['zele', 'apple'])}"]
        actual_result = str(plantation)
        expected_result = "\n".join(to_join)
        self.assertEqual(expected_result, actual_result)




