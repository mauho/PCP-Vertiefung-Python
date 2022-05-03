from unittest import TestCase
from pcp import main


class Test(TestCase):
    def test_add(self):
        self.assertEqual(main.add(21, 21), 42)


