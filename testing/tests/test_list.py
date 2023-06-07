from labs.list import IntegerList

from unittest import TestCase, main


class TestList(TestCase):
    def setUp(self) -> None:
        self.lst_int = IntegerList(1, "5", 2, 5.5, 6)
        self.lst = [1, 2, 6]

    def test__init_expect_only_integers(self):
        self.assertEqual(self.lst, self.lst_int._IntegerList__data)

    def test__get_data_expect_list_of_ints(self):
        integers = self.lst_int.get_data()
        self.assertEqual(self.lst, integers)

    def test__add_expect_raise_when_not_int(self):
        with self.assertRaises(ValueError) as error:
            self.lst_int.add("5")

        self.assertIsNotNone(error)
        self.assertEqual("Element is not Integer", str(error.exception))

    def test__add_expect_int_to_add(self):
        self.lst_int.add(3)
        self.assertEqual([1, 2, 6, 3], self.lst_int.get_data())

    def test__remove__when_idx_out_of_range_expect_raise(self):
        with self.assertRaises(IndexError) as error:
            self.lst_int.remove_index(10)

        self.assertIsNotNone(error)
        self.assertEqual("Index is out of range", str(error.exception))

    def test__remove__when_idx_in_range_expect_removed_item(self):
        self.lst_int.remove_index(0)
        self.assertEqual([2, 6], self.lst_int.get_data())

    def test__get__when_idx_out_of_range_expect_raise(self):
        with self.assertRaises(IndexError) as error:
            self.lst_int.get(10)

        self.assertIsNotNone(error)
        self.assertEqual("Index is out of range", str(error.exception))

    def test__get_when_idx_in_range_expect_element(self):
        element = self.lst_int.get(0)
        self.assertEqual(1, element)

    def test__insert__when_idx_out_of_range_expect_raise(self):
        with self.assertRaises(IndexError) as error:
            self.lst_int.insert(10, 5)

        self.assertIsNotNone(error)
        self.assertEqual("Index is out of range", str(error.exception))

    def test__insert_when_element_is_not_int_expect_raise(self):
        with self.assertRaises(ValueError) as error:
            self.lst_int.insert(2, "4")

        self.assertIsNotNone(error)
        self.assertEqual("Element is not Integer", str(error.exception))

    def test__insert_expect_element_to_be_added(self):
        self.lst_int.insert(2, 5)
        expected_value = self.lst_int.get_data()[2]
        self.assertEqual(expected_value, 5)

    def test__get_biggest__expect_largest_value(self):
        expected_value = 6
        actual_value = self.lst_int.get_biggest()
        self.assertEqual(expected_value, actual_value)

    def test__get_index_expect_value(self):
        expected_value = 1
        actual_value = self.lst_int.get_index(2)
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    main()