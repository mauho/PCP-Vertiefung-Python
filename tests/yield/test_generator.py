from unittest import TestCase
from src.generator.generator import *


class Test(TestCase):

    def test_fib(self):
        generator = fib_generator(5)
        generator.__next__()
        self.assertEqual(1, generator.__next__())

    def test_fib_3(self):
        generator = fib_generator(5)
        generator.__next__()
        generator.__next__()
        generator.__next__()
        generator.__next__()
        self.assertEqual(3, generator.__next__())
