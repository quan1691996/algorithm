"""
Selection Sort
"""
import unittest


def insertion_sort(array: list):
    for step in range(len(array)):
        min = step
        for i in range(step+1,len(array)):
            if array[min]>array[i]:
                min = i
        array[min], array[step] = array[step], array[min]


class TestInsertionSort(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.integers = [6, 8, 10, 26, 9, 2, 40, 22, 5, 32, 3]
        self.strings = ["c", "assembly", "cpp", "python", "go", "swift", "sql"]
        self.floats = [5.2, 4.4, 6.8, 9.5, 0.7, 1.2, 3.2, 5.9]

    def test_handles_multiple_array_type_input(self):
        insertion_sort(self.integers)
        self.assertListEqual(self.integers, [2, 3, 5, 6, 8, 9, 10, 22, 26, 32, 40])
        insertion_sort(self.strings)
        self.assertListEqual(
            self.strings, ["assembly", "c", "cpp", "go", "python", "sql", "swift"]
        )
        insertion_sort(self.floats)
        self.assertListEqual(self.floats, [0.7, 1.2, 3.2, 4.4, 5.2, 5.9, 6.8, 9.5])


if __name__ == "__main__":
    unittest.main()