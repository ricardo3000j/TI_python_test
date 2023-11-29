from typing import List


class Statistics:
    """Statistic class - generate statistic object to get statistics of counter array

    attributes:
    - cumulative_sum: array for cumulative sum of counter array values

    methods:
    - less(number): return number of values less than number
    - greater(number): return number of values greater than number
    - between(start, end): return number of values between start and end numbers
    complexity - O(1) since to calculate the statistic we use only index of array instead of iterate over whole array
    """

    def __init__(self, counters: List[int]) -> None:
        self.cumulative_sum: List[int] = counters

    def less(self, number: int) -> int:
        if validate_input(number):
            return self.cumulative_sum[number - 1]

    def greater(self, number: int) -> int:
        if validate_input(number):
            return self.cumulative_sum[-1] - self.cumulative_sum[number]

    def between(self, start: int, end: int) -> int:
        if validate_input(start) and validate_input(end):
            return self.cumulative_sum[-1] - (self.less(start) + self.greater(end))


class DataCapture:
    """Data capture class - store positive integer values and generate statistics object
    Attributes:
    - counter: counter array for integer numbers.
    - cumulative_sum: array for cumulative sum of counter array values

    Methods:
    - add(value): add positive integer value to counter array, increasing the counting of occurrences of the value
    - build_stats(): generate statistic object to calculate statistics of counter array
    """

    def __init__(self) -> None:
        self.counter: List[int] = [0] * 1000
        self.cumulative_sum: List[int] = [0] * 1000

    def add(self, value) -> None:
        if validate_input(value):  # check if value is positive integer
            self.counter[value] += 1

    def build_stats(self) -> Statistics:
        self.cumulative_sum[0] = self.counter[0]
        for index in range(
            1, len(self.counter)
        ):  # calculate cumulative sum of counter array
            self.cumulative_sum[index] = (
                self.cumulative_sum[index - 1] + self.counter[index]
            )
        return Statistics(self.cumulative_sum)


def validate_input(input_value):
    if isinstance(input_value, int) and input_value >= 0:
        return True
    else:
        return False
