"""
Merge Sort
"""
import unittest
 
 
def merge(arr: list, l: int, m: int, r: int):
    L = arr[l:m+1]
    R = arr[m+1:r+1]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
 
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
 
def merge_sort(arr: list, l: int, r: int):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)

class TestMergeSort(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.integers = [6, 8, 10, 26, 9, 2, 40, 22, 5, 32, 3]
        self.strings = ["c", "assembly", "cpp", "python", "go", "swift", "sql"]
        self.floats = [5.2, 4.4, 6.8, 9.5, 0.7, 1.2, 3.2, 5.9]

    def test_handles_multiple_array_type_input(self):
        merge_sort(self.integers,0,len(self.integers)-1)
        self.assertListEqual(self.integers, [2, 3, 5, 6, 8, 9, 10, 22, 26, 32, 40])
        merge_sort(self.strings,0,len(self.strings)-1)
        self.assertListEqual(
            self.strings, ["assembly", "c", "cpp", "go", "python", "sql", "swift"]
        )
        merge_sort(self.floats,0,len(self.floats)-1)
        self.assertListEqual(self.floats, [0.7, 1.2, 3.2, 4.4, 5.2, 5.9, 6.8, 9.5])


if __name__ == "__main__":
    unittest.main()