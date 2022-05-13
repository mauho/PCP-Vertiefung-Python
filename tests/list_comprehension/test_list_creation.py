from unittest import TestCase
from src.list_comprehension.list_creation import *


class Test(TestCase):

    threes = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

    def test_get_divisible_numbers_imp(self):
        self.assertEqual(get_divisible_numbers_imp(3, 30), self.threes)

    def test_get_divisible_numbers_func(self):
        self.assertEqual(get_divisible_numbers_func(3, 30), self.threes)
