from unittest import TestCase
from src.list_comprehension.sw9_ex4_string_join import *


class Test(TestCase):

    reference = "Python is also an Animal"
    reference_list = reference.split()

    def test_join_string_imp(self):
        result = join_string_imp(self.reference_list)
        self.assertEqual(self.reference, result)

    def test_join_string_func(self):
        result = join_string_func(self.reference_list)
        self.assertEqual(self.reference, result)
