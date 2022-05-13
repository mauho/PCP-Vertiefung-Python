from unittest import TestCase
from src.concurrency.sw09_ex3_completable_future import *
from unittest.mock import patch


def measure_exec_time(function, *args) -> float:
    """
    Returns the execution time for the given function + arguments
    :param function: function to execute
    :param args: arguments for the function
    :return: execution time in millis
    """
    start = time.perf_counter()
    function(*args)
    return time.perf_counter() - start


class Test(TestCase):
    """
    Tests for a part of the completable future exercise to figure how we can catch stdout and include it in a test.
    """
    def test_do_blocking_wait(self):
        execution_time = measure_exec_time(do_blocking_wait, 200)
        self.assertTrue(execution_time < 203)

    @patch('builtins.print')
    def test_long_lasting_task(self, mock_print):
        execution_time = measure_exec_time(long_lasting_task)
        self.assertTrue(execution_time < 3003)
        mock_print.assert_called_with('3000', end='')
