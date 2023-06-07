from project.movie import Movie
from unittest import TestCase

# from movie import Movie


class MovieTest(TestCase):
    NAME = "The Labyrinth"
    YEAR = 2004
    RATING = 8
    MIN_YEAR = 1887

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test__init__expect_valid_attributes(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test__setter_for_name_when_empty_string_expect_raise(self):
        with self.assertRaises(ValueError) as error:
            self.movie.name = ""

        self.assertIsNotNone(error)
        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test__setter_for_year_when_it_is_too_old_expect_raise(self):
        with self.assertRaises(ValueError) as error:
            self.movie.year = self.MIN_YEAR - 10

        self.assertIsNotNone(error)
        self.assertEqual("Year is not valid!", str(error.exception))

    def test__add_actor__expect_two_different_actors_to_be_added(self):
        first = "Pesho"
        second = "Vasko"
        self.movie.add_actor(first)
        self.movie.add_actor(second)
        expected_value = [first, second]
        self.assertEqual(expected_value, self.movie.actors)

    def test__add_actor__when_two_actors_with_the_same_name(self):
        actor = "Vasko"
        self.movie.actors.append(actor)
        result = self.movie.add_actor(actor)
        self.assertEqual(f"{actor} is already added in the list of actors!", result)
        self.assertEqual([actor], self.movie.actors)

    def test__gt__expect_correct_calculation(self):
        other_movie = Movie("Nemo", 2005, 9)
        result = other_movie > self.movie
        self.assertEqual(f'"{other_movie.name}" is better than "{self.movie.name}"', result)
        result = self.movie > other_movie
        self.assertEqual(f'"{other_movie.name}" is better than "{self.movie.name}"', result)

    def test__repr__expect_correct_result(self):
        actors = ["pesho", "vasko"]
        self.movie.actors = actors
        expected_result = f"Name: {self.movie.name}\n" \
               f"Year of Release: {self.movie.year}\n" \
               f"Rating: {self.movie.rating:.2f}\n" \
               f"Cast: {', '.join(self.movie.actors)}"
        actual_result = repr(self.movie)
        self.assertEqual(expected_result, actual_result)
