from OOP.exam_preparation.test_projects.project_test_team.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("lords")

    def test_initialisation(self):
        self.assertEqual("lords", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_if_name_setter_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "team_name"

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_if_add_memer_func_adds_to_the_dict(self):
        self.team.members = {"Ivan": 20, "Gosho": 25}
        members = {"pesho": 21, "Ivan": 20, "ceco": 23}
        actual_result = self.team.add_member(**members)
        expected_return_result = "Successfully added: pesho, ceco"

        self.assertEqual(expected_return_result, actual_result)
        self.assertEqual({"Ivan": 20, "Gosho": 25, "pesho": 21, "ceco": 23}, self.team.members)

    def test_if_add_members_func_doesnt_add_to_func(self):
        self.team.members = {"Ivan": 20, "Gosho": 25}
        members = {"Ivan": 20, "Gosho": 25}
        actual_result = self.team.add_member(**members)
        expected_result = "Successfully added: "
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({"Ivan": 20, "Gosho": 25}, self.team.members)

    def test_another_thing_for_this_stupid_function(self):
        members = {"pesho": 21, "Ivan": 20, "ceco": 23}
        actual_result = self.team.add_member(**members)
        expected_return_result = "Successfully added: pesho, Ivan, ceco"
        self.assertEqual(expected_return_result, actual_result)
        self.assertEqual({"pesho": 21, "Ivan": 20, "ceco": 23}, self.team.members)

    def test_if_add_memer_func_adds_to_the_dict(self):
        self.team.members = {"Ivan": 20, "Gosho": 25}
        actual_result = self.team.add_member(pesho=21, ceco=23)
        expected_return_result = "Successfully added: pesho, ceco"

        self.assertEqual(expected_return_result, actual_result)
        self.assertEqual({"Ivan": 20, "Gosho": 25, "pesho": 21, "ceco": 23}, self.team.members)

    def test_if_remove_func_removes_from_the_dict_and_returns_correct_result(self):
        self.team.members = {"Ivan": 20, "Gosho": 25, "pesho": 21}
        actual_return_result = self.team.remove_member("Ivan")
        expected_return_result = "Member Ivan removed"

        self.assertEqual(expected_return_result, actual_return_result)
        self.assertEqual({"Gosho": 25, "pesho": 21}, self.team.members)

    def test_if_remove_func_returns_correct_info_for_non_existing_name(self):
        self.team.members = {"Ivan": 20, "Gosho": 25, "pesho": 21}
        actual_return_result = self.team.remove_member("Ceco")
        expected_return_result = "Member with name Ceco does not exist"

        self.assertEqual(expected_return_result, actual_return_result)
        self.assertEqual({"Ivan": 20, "Gosho": 25, "pesho": 21}, self.team.members)

    def test_if_gt_func_is_overriden_correctly_and_returns_true(self):
        second_team = Team("Rings")
        self.team.members = {"Ivan": 20, "Gosho": 25, "pesho": 21}
        second_team.members = {"Ivan": 20, "Gosho": 25}

        actual_result = self.team > second_team
        expected_result = True
        self.assertEqual(expected_result, actual_result)

    def test_if_gt_func_is_overriden_correctly_and_returns_false(self):
        second_team = Team("Rings")
        self.team.members = {"Ivan": 20, "Gosho": 25}
        second_team.members = {"Ivan": 20, "Gosho": 25, "pesho": 21}

        actual_result = self.team > second_team
        expected_result = False
        self.assertEqual(expected_result, actual_result)

    def test_if_len_func_is_overriden_correctly(self):
        self.team.members = {"Ivan": 20, "Gosho": 25, "pesho": 21}

        actual_result = len(self.team)
        expected_result = 3
        self.assertEqual(expected_result, actual_result)

    def test_if_add_func_is_overriden_correctly(self):
        second_team = Team("Rings")
        self.team.members = {"Ivan": 20, "Gosho": 25, "pesho": 21}
        second_team.members = {"ceco": 20, "stanimir": 25}
        new_team = self.team + second_team

        self.assertEqual("lordsRings", new_team.name)
        self.assertEqual({"Ivan": 20, "Gosho": 25, "pesho": 21, "ceco": 20, "stanimir": 25}, new_team.members)
        # do I need to test the return ?

    def test_if_str_method_is_overriden_correctly(self):
        self.team.members = {"Ivan": 20, "Gosho": 25, "pesho": 21, "ceco": 28, "stanimir": 28}
        actual_result = str(self.team)
        expected_result = "Team name: lords\n" \
                          "Member: ceco - 28-years old\n" \
                          "Member: stanimir - 28-years old\n" \
                          "Member: Gosho - 25-years old\n" \
                          "Member: pesho - 21-years old\n" \
                          "Member: Ivan - 20-years old"

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
