from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("ally", 15, 1000, 100)
        # self.enemy = Hero("enemy", 15, 1000, 100)

    def test__init__expect_correct_values(self):
        self.assertEqual("ally", self.hero.username)
        self.assertEqual(15, self.hero.level)
        self.assertEqual(1000, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test__battle__expect_fighting_yourself_raise(self):
        with self.assertRaises(Exception) as error:
            self.hero.battle(self.hero)

        self.assertIsNotNone(error)
        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test__battle_when_hp_no_hp_expect_raise(self):
        enemy = Hero("enemy", 15, 1000, 100)
        self.hero.health = 0
        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy)

        self.assertIsNotNone(error)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test__battle_when_enemy_no_hp_low_expect_raise(self):
        enemy = Hero("enemy", 15, -10, 100)
        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy)

        self.assertIsNotNone(error)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(error.exception))

    def test__battle__expect_both_heroes_below_0(self):
        enemy = Hero("enemy", 15, 1000, 100)
        expected_value = "Draw"
        actual_value = self.hero.battle(enemy)
        self.assertEqual(-500, self.hero.health)
        self.assertEqual(-500, enemy.health)
        self.assertEqual(expected_value, actual_value)

    def test__battle__expect_enemy_to_die(self):
        enemy = Hero("enemy", 1, 1, 1)
        expected_hp = self.hero.health + 5 - enemy.damage * enemy.level
        expected_value = "You win"
        actual_value = self.hero.battle(enemy)
        self.assertEqual(16, self.hero.level)
        self.assertEqual(expected_hp, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual(expected_value, actual_value)

    def test__battle__when_self_dies(self):
        enemy = Hero("enemy", 15, 1000, 100)
        self.hero.level, self.hero.health, self.hero.damage = 1, 1, 1
        expected_hp = enemy.health + 5 - self.hero.damage * self.hero.level
        expected_value = "You lose"
        actual_value = self.hero.battle(enemy)
        self.assertEqual(16, enemy.level)
        self.assertEqual(expected_hp, enemy.health)
        self.assertEqual(105, enemy.damage)
        self.assertEqual(expected_value, actual_value)

    def test__str__expect_value_to_return(self):
        expected_value = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        actual_value = self.hero.__str__()
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    main()

