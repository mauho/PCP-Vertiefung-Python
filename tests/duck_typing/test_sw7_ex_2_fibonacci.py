from unittest import TestCase
from src.duck_typing.performance_check import fib


class Test(TestCase):

    def test_fib_number_3(self):
        result = fib(3)
        self.assertEqual(2, result)

    def test_fib_number_7(self):
        result = fib(7)
        self.assertEqual(13, result)

    def test_fib_number_11(self):
        result = fib(11)
        self.assertEqual(89, result)

    def test_fib_accumulator_number_3(self):
        result = fib(3)
        self.assertEqual(2, result)

    def test_fib_accumulator_number_7(self):
        result = fib(7)
        self.assertEqual(13, result)

    def test_fib_accumulator_number_11(self):
        result = fib(11)
        self.assertEqual(89, result)
