import unittest
from data_capture import DataCapture


class TestDataCapture(unittest.TestCase):
    """Test cases for DataCapture Methods"""

    def test_add_new_value(self):
        capture = DataCapture()
        capture.add(5)
        self.assertEqual(capture.counter[5], 1)

    def test_add_existing_value(self):
        capture = DataCapture()
        capture.counter[5] = 2
        capture.add(5)
        self.assertEqual(capture.counter[5], 3)

    def test_add_multiple_values(self):
        capture = DataCapture()
        capture.add(1)
        capture.add(2)
        capture.add(1)
        expected_counter = [0] * 1000
        expected_counter[1] = 2
        expected_counter[2] = 1
        self.assertEqual(capture.counter, expected_counter)

    def test_add_negative_value(self):
        capture = DataCapture()
        capture.add(-1)
        expected_counter = [0] * 1000
        self.assertEqual(capture.counter, expected_counter)

    def test_add_zero_value(self):
        capture = DataCapture()
        capture.add(0)
        self.assertEqual(capture.counter[0], 1)

    def test_add_not_integer_value(self):
        capture = DataCapture()
        capture.add("a")
        expected_counter = [0] * 1000
        self.assertEqual(capture.counter, expected_counter)

    def test_empty_counter(self):
        capture = DataCapture()
        expected_counter = [0] * 1000
        self.assertEqual(capture.counter, expected_counter)

    def test_cumulative_sum(self):
        capture = DataCapture()
        capture.add(1)
        capture.add(2)
        capture.add(1)
        expected_cumulative_sum = [0] * 1000
        expected_cumulative_sum[1] = 2
        expected_cumulative_sum[2] = 3
        expected_cumulative_sum[3:] = [3] * 997
        stats = capture.build_stats()
        self.assertEqual(stats.cumulative_sum, expected_cumulative_sum)

    def test_cumulative_sum_empty(self):
        capture = DataCapture()
        expected_cumulative_sum = [0] * 1000
        stats = capture.build_stats()
        self.assertEqual(stats.cumulative_sum, expected_cumulative_sum)


class TestStatistics(unittest.TestCase):
    """Test cases for Statistics Methods"""

    def test_greater(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        self.assertEqual(capture.build_stats().greater(4), 1)

    def test_greater_empty(self):
        capture = DataCapture()
        self.assertEqual(capture.build_stats().greater(4), 0)

    def test_greater_empty_2(self):
        capture = DataCapture()
        capture.add(3)
        self.assertEqual(capture.build_stats().greater(4), 0)

    def test_greater_not_integer_value(self):
        capture = DataCapture()
        capture.add("a")
        self.assertEqual(capture.build_stats().greater(4), 0)

    def test_greater_negative_value(self):
        capture = DataCapture()
        capture.add(-5)
        self.assertEqual(capture.build_stats().greater(4), 0)

    def test_less(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        self.assertEqual(capture.build_stats().less(4), 2)

    def test_less_empty(self):
        capture = DataCapture()
        self.assertEqual(capture.build_stats().less(4), 0)

    def test_less_empty_2(self):
        capture = DataCapture()
        capture.add(6)
        self.assertEqual(capture.build_stats().less(4), 0)

    def test_less_not_integer_value(self):
        capture = DataCapture()
        capture.add("a")
        self.assertEqual(capture.build_stats().less(4), 0)

    def test_less_negative_value(self):
        capture = DataCapture()
        capture.add(-5)
        self.assertEqual(capture.build_stats().less(4), 0)

    def test_between(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        self.assertEqual(capture.build_stats().between(3, 6), 4)

    def test_between_empty(self):
        capture = DataCapture()
        self.assertEqual(capture.build_stats().between(3, 6), 0)

    def test_between_empty_2(self):
        capture = DataCapture()
        capture.add(2)
        capture.add(7)
        self.assertEqual(capture.build_stats().between(3, 6), 0)

    def test_between_not_integer_value(self):
        capture = DataCapture()
        capture.add("a")
        self.assertEqual(capture.build_stats().between(3, 6), 0)

    def test_between_negative_value(self):
        capture = DataCapture()
        capture.add(-5)
        self.assertEqual(capture.build_stats().between(3, 6), 0)


if __name__ == "__main__":
    unittest.main()
