import unittest
from Level2.solution import solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution('210022', 3), 3)
        self.assertEqual(solution('1211', 10), 1)
