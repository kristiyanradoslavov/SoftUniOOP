from unittest import TestCase, main

from OOP.testing.testing_exercise.projects_to_test.project_hero.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("ramune", 16, 85.5, 150)
        self.enemy = Hero("psihokiller", 20, 100, 100)

    def test_initialization(self):
        self.assertEqual("ramune", self.hero.username)
        self.assertEqual(16, self.hero.level)
        self.assertEqual(85.5, self.hero.health)
        self.assertEqual(150, self.hero.damage)

    def test_if_equal_name_with_the_enemy_raises_error(self):
        self.enemy.username = "ramune"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_if_own_health_bellow_zero_raises_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_if_enemy_health_bellow_zero_raises_value_error(self):
        self.enemy.health = -5

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight psihokiller. He needs to rest", str(ve.exception))

    def test_if_own_health_is_decreased_with_enemy_damage(self):
        enemy_damage = self.enemy.damage * self.enemy.level
        expected_result = self.hero.health - enemy_damage

        self.hero.battle(self.enemy)
        self.assertEqual(self.hero.health, expected_result)

    def test_if_enemy_health_is_decreased_with_own_damage(self):
        player_damage = self.hero.damage * self.hero.level
        expected_result = self.enemy.health - player_damage

        self.hero.battle(self.enemy)
        self.assertEqual(self.enemy.health, expected_result)

    def test_if_the_func_returns_draw_when_both_the_players_are_bellow_or_equal_to_zero(self):
        self.hero.health = 100
        self.hero.level = 10
        self.enemy.health = 100
        self.enemy.level = 10

        expected_result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", expected_result)

    def test_if_hero_wins_and_the_health_of_the_enemy_is_bellow_zero(self):
        self.hero.health = 1000
        self.hero.level = 1000
        self.enemy.health = 1
        self.enemy.level = 1
        expected_result = self.hero.battle(self.enemy)

        self.assertEqual("You win", expected_result)

    def test_if_enemy_wins_and_the_health_of_the_hero_is_bellow_zero(self):
        self.hero.health = 1
        self.hero.level = 1
        self.enemy.health = 1000
        self.enemy.level = 1000
        expected_result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", expected_result)

    def test_if_the_stats_of_the_hero_are_increased_when_he_wins(self):
        self.hero.health = 1000
        self.hero.level = 1000
        self.enemy.health = 1
        self.enemy.level = 1

        enemy_damage = self.enemy.damage * self.enemy.level
        expected_health = self.hero.health - enemy_damage + 5

        self.hero.battle(self.enemy)

        self.assertEqual(1001, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(155, self.hero.damage)

    def test_if_the_stats_of_the_enemy_are_increased_when_he_wins(self):
        self.hero.health = 1
        self.hero.level = 1
        self.enemy.health = 1000
        self.enemy.level = 1000

        hero_damage = self.hero.damage * self.hero.level
        expected_health = self.enemy.health - hero_damage + 5

        self.hero.battle(self.enemy)

        self.assertEqual(1001, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)

    def test_if_the_str_func_is_replaced_and_if_returns_expected_result(self):
        expected_result = f"Hero ramune: 16 lvl\n" \
                          f"Health: 85.5\n" \
                          f"Damage: 150\n"

        actual_result = str(self.hero)
        self.assertEqual(expected_result, actual_result)


if "__main__" == __name__:
    main()
