"""
Counting Sort
"""
import unittest

def counting_sort(array: list, max: int) -> None:
    size = len(array)
    output = [0] * size

    count = [0] * max

    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, max):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

class TestCountingSort(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.integers = [6, 8, 10, 26, 9, 2, 40, 22, 5, 32, 3]
        self.strings = ["c", "assembly", "cpp", "python", "go", "swift", "sql"]
        self.floats = [5.2, 4.4, 6.8, 9.5, 0.7, 1.2, 3.2, 5.9]

    def test_handles_multiple_array_type_input(self):
        counting_sort(self.integers, 50)
        self.assertListEqual(self.integers, [2, 3, 5, 6, 8, 9, 10, 22, 26, 32, 40])


if __name__ == "__main__":
    unittest.main()