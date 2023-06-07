from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    def test__init_when_courses_are_None(self):
        student = Student("Vasko")
        self.assertEqual("Vasko", student.name)
        self.assertIsNotNone(student.courses)

    def test__init_when_course_are_present(self):
        student = Student("Vasko", {"Python": [1, 2, 3]})
        to_be_true = isinstance(student.courses, dict)
        self.assertEqual("Vasko", student.name)
        self.assertTrue(to_be_true)

    def test__enroll_expect_to_add_a_not_in_an_existing_course(self):
        student = Student("Vasko", {"Python": [1, 2, 3]})
        returned_value = student.enroll("Python", [4, 5])
        expected_value = {"Python": [1, 2, 3, 4, 5]}
        self.assertEqual(expected_value, student.courses)
        self.assertEqual("Course already added. Notes have been updated.", returned_value)

    def test__enroll_when_notes_are_presented_expect_to_add_them(self):
        student = Student("Vasko", {"Python": [1, 2, 3]})
        returned_value = student.enroll("Java", ["J", "A", "V", "A"], "")
        expected_value = {"Python": [1, 2, 3], "Java": ["J", "A", "V", "A"]}
        self.assertEqual(expected_value, student.courses)
        self.assertEqual("Course and course notes have been added.", returned_value)

    def test__enroll_when_notes_are_presented_expect_to_add_them_with_Y(self):
        student = Student("Vasko", {"Python": [1, 2, 3]})
        returned_value = student.enroll("Java", ["J", "A", "V", "A"], "Y")
        expected_value = {"Python": [1, 2, 3], "Java": ["J", "A", "V", "A"]}
        self.assertEqual(expected_value, student.courses)
        self.assertEqual("Course and course notes have been added.", returned_value)

    def test__enroll__expect_empty_notes(self):
        student = Student("Vasko", {"Python": [1, 2, 3]})
        returned_value = student.enroll("Java", ["J", "A", "V", "A"], "N")
        expected_value = {"Python": [1, 2, 3], "Java": []}
        self.assertEqual(expected_value, student.courses)
        self.assertEqual("Course has been added.", returned_value)

    def test__add_notes_when_course_exists_expect_extension(self):
        student = Student("Vasko", {"Python": [1, 2, 3]})
        returned_value = student.add_notes("Python", "i love python")
        expected_value = {"Python": [1, 2, 3, "i love python"]}
        self.assertEqual(expected_value, student.courses)
        self.assertEqual("Notes have been updated", returned_value)

    def test__add_notes_when_the_course_does_note_exist_expect_raise(self):
        student = Student("Vasko", {"Python": [1, 2, 3]})
        with self.assertRaises(Exception) as error:
            student.add_notes("Java", ["J", "A", "V", "A"])

        self.assertIsNotNone(error)
        self.assertEqual("Cannot add notes. Course not found.", str(error.exception))

    def test__leave_course_when_course_exists_expect_removal(self):
        student = Student("Vasko", {"Python": [1, 2, 3]})
        returned_value = student.leave_course("Python")
        self.assertEqual(dict(), student.courses)
        self.assertEqual("Course has been removed", returned_value)

    def test__leave_course_when_we_are_not_enrolled_expect_raise(self):
        student = Student("Vasko", {"Python": [1, 2, 3]})
        with self.assertRaises(Exception) as error:
            student.leave_course("Java")

        self.assertIsNotNone(error)
        self.assertEqual("Cannot remove course. Course not found.", str(error.exception))


if __name__ == "__main__":
    main()
