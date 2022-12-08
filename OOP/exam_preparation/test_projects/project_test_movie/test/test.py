from OOP.exam_preparation.test_projects.project_test_movie.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Inception", 2005, 9.99)

    def test_initialization(self):
        self.assertEqual("Inception", self.movie.name)
        self.assertEqual(2005, self.movie.year)
        self.assertEqual(9.99, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_if_name_setter_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_if_year_setter_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1800

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_if_add_actor_adds_to_the_list(self):
        self.movie.actors = ["ivan", "zahari"]
        self.movie.add_actor("gosho")

        self.assertEqual(["ivan", "zahari", "gosho"], self.movie.actors)

    def test_if_add_actor_returns_correct_result(self):
        self.movie.actors = ["ivan", "zahari"]
        actual_result = self.movie.add_actor("ivan")
        expected_result = "ivan is already added in the list of actors!"

        self.assertEqual(expected_result, actual_result)

    def test_if_overriding_gt_returns_correct_result_when_the_first_rating_is_greater(self):
        movie2 = Movie("Interstellar", 2010, 10.00)

        actual_result = self.movie > movie2
        expected_result = '"Interstellar" is better than "Inception"'
        self.assertEqual(expected_result, actual_result)

    def test_if_overriding_gt_returns_correct_result_when_the_second_rating_is_greater(self):
        movie2 = Movie("Interstellar", 2010, 9.20)

        actual_result = self.movie > movie2
        expected_result = '"Inception" is better than "Interstellar"'
        self.assertEqual(expected_result, actual_result)

    def test_if_repr_is_overriden_correctly(self):
        self.movie.actors = ["ivan", "zahari", "gosho"]
        actual_result = repr(self.movie)
        expected_result = "Name: Inception\n" \
                          "Year of Release: 2005\n" \
                          "Rating: 9.99\n" \
                          "Cast: ivan, zahari, gosho"

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
