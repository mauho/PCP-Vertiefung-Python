from unittest import TestCase
from unittest.mock import patch

from src.concurrency.threads_vs_processes import *


def sum_int(a: int, b: int) -> int:
    return a + b


class Test(TestCase):

    @patch('builtins.print')
    def test_time_measurement(self, mock_print):
        res = time_measurement(sum_int, 1, 2)
        self.assertEqual(res, 3)
        mock_print.assert_called_with('sum_int took 0.00 seconds')
