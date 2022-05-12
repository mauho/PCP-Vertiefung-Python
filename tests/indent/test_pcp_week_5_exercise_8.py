from unittest import TestCase
from src.indent.pcp_week_5_exercise_8 import Human, b_length


class Test(TestCase):

    def test_height_male_human_29(self):
        male_human = Human("m", 29, 45)
        self.assertEqual(b_length(male_human), 169.8)

    def test_height_male_human_50(self):
        male_human = Human("m", 50, 45)
        self.assertEqual(b_length(male_human), 168.6)

    def test_height_female_human_29(self):
        female_human = Human("w", 29, 45)
        self.assertEqual(b_length(female_human), 165.68)

    def test_height_female_human_50(self):
        female_human = Human("w", 50, 45)
        self.assertEqual(b_length(female_human), 164.48)
