from unittest import TestCase, main
from OOP.testing.testing_exercise.projects_to_test.project_student.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Ivan", {"matematika": ["zapiska_1"]})
        self.student_none = Student("Ivan")

    def test_initialising_with_courses_equal_to_none(self):
        self.assertEqual({}, self.student_none.courses)

    def test_initialising_with_all_parameters_filled(self):
        self.assertEqual("Ivan", self.student.name)
        self.assertEqual({"matematika": ["zapiska_1"]}, self.student.courses)

    def test_if_notes_are_added_to_the_courses_dict_when_the_course_exists(self):
        self.student.enroll("matematika", ['zapiska_2', 'zapiska_3'], "Y")
        expected_result = {"matematika": ["zapiska_1", 'zapiska_2', 'zapiska_3']}
        self.assertEqual(expected_result, self.student.courses)

    def test_if_enrol_returns_expected_result_when_the_key_exists_and_we_add_new_notes(self):
        expected_result = self.student.enroll("matematika", ['zapiska_2', 'zapiska_3'])
        self.assertEqual(expected_result, "Course already added. Notes have been updated.")

    def test_if_adding_new_key_and_new_notes_works_when_the_add_course_notes_is_y(self):
        self.student.enroll("biologiq", ['zapiska_2', 'zapiska_3'], "Y")
        expected_result = {"matematika": ["zapiska_1"], "biologiq": ['zapiska_2', 'zapiska_3']}
        self.assertEqual(expected_result, self.student.courses)

    def test_if_adding_new_key_and_new_notes_works_when_the_add_course_notes_is_empty_string(self):
        self.student.enroll("biologiq", ['zapiska_2', 'zapiska_3'])
        expected_result = {"matematika": ["zapiska_1"], "biologiq": ['zapiska_2', 'zapiska_3']}
        self.assertEqual(expected_result, self.student.courses)

    def test_if_adding_new_key_and_new_notes_returns_the_correct_information(self):
        expected_result = self.student.enroll("biologiq", ['zapiska_2', 'zapiska_3'])
        self.assertEqual(expected_result, "Course and course notes have been added.")

    def test_if_the_course_is_being_added_when_the_key_doesnt_exist_in_the_dict(self):
        self.student_none.enroll("biologiq", ['zapiska_2', 'zapiska_3'], "N")
        expected_result = {"biologiq": []}
        self.assertEqual(expected_result, self.student_none.courses)

    def test_if_courses_enrol_returns_correct_info_when_the_key_is_not_in_the_dict_and_the_last_str_is_empt(self):
        expected_result = self.student_none.enroll("biologiq", ['zapiska_2', 'zapiska_3'], "N")
        self.assertEqual(expected_result, "Course has been added.")

    def test_if_notes_have_been_added_to_the_dict_when_the_key_exists(self):
        self.student.add_notes("matematika", 'zapiska_2')
        expected_result = {"matematika": ["zapiska_1", 'zapiska_2']}
        self.assertEqual(expected_result, self.student.courses)

    def test_if_add_notes_func_returns_correct_result_when_the_key_exists(self):
        expected_result = self.student.add_notes("matematika", 'zapiska_2')
        self.assertEqual(expected_result, "Notes have been updated")

    def test_if_add_notes_raises_exception_when_the_key_doesnt_exist(self):
        with self.assertRaises(Exception)as ex:
            self.student.add_notes("biologiq", 'zapiska_2')

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_if_leave_course_func_removes_a_key_when_it_exists(self):
        self.student.leave_course("matematika")
        expected_result = {}
        self.assertEqual(expected_result, self.student.courses)

    def test_if_leave_course_func_returns_the_correct_result_when_it_removes_a_key_which_exists(self):
        expected_result = self.student.leave_course("matematika")
        self.assertEqual(expected_result, "Course has been removed")

    def test_if_leave_course_func_raises_exception_when_we_try_to_remove_a_key_which_does_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("biologia")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if "__main__" == __name__:
    main()
