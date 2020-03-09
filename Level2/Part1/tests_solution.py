import unittest
from Level2.solution import solution, get_cycle_length, _get_x_and_y_strings, _convert_base_10_int_to_base_n_string


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution('210022', 3), 3)
        self.assertEqual(solution('1211', 10), 1)

    def test_check_cycle_length_repeating_constant(self):
        self.assertEquals(get_cycle_length(45, [21, 35, 45]), 1)

    def test_check_cycle_no_cycle(self):
        self.assertEquals(get_cycle_length(46, [21, 35, 45]), 0)

    def test_check_cycle_cycle(self):
        self.assertEquals(get_cycle_length(46, [46, 35, 45]), 3)
        self.assertEquals(get_cycle_length(46, [46, 45]), 2)
        self.assertEquals(get_cycle_length(46, [882, 1, 35, 46, 45, 5, 3]), 4)

    def test_get_x_and_y(self):
        self.assertEquals(_get_x_and_y_strings(
            44572110), ("75442110", "01124457"))

    def test_convert_base_10_int_to_base(self):
        self.assertEquals(_convert_base_10_int_to_base_n_string(24, 3), "220")
        self.assertEquals(_convert_base_10_int_to_base_n_string(89, 4), "1121")
        self.assertEquals(
            _convert_base_10_int_to_base_n_string(5000, 5), "130000")
        self.assertEquals(
            _convert_base_10_int_to_base_n_string(239384, 6), "5044132")
        self.assertEquals(_convert_base_10_int_to_base_n_string(
            29394, 2), "111001011010010")
