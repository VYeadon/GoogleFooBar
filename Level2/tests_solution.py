import unittest
from Level2.solution import solution, check_cycle_length


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution('210022', 3), 3)
        self.assertEqual(solution('1211', 10), 1)

    def test_check_cycle_length_repeating_constant(self):
        self.assertEquals(check_cycle_length(12345, 45, [21, 35, 45]), 1)

    def test_check_cycle_no_cycle(self):
        self.assertEquals(check_cycle_length(12345, 46, [21, 35, 45]), 0)

    def test_check_cycle_cycle(self):
        self.assertEquals(check_cycle_length(12345, 46, [46, 35, 45]), 3)
        self.assertEquals(check_cycle_length(12345, 46, [46, 45]), 2)
        self.assertEquals(check_cycle_length(12345, 46, [46, 45, 5, 3]), 4)
