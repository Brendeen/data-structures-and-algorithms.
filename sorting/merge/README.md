# Blog Notes: Merge Sort

![Merge sort](Screenshot%202023-06-16%20at%201.38.11%20PM.png)

Here are a few provided tests to run-

  import pytest

def test_merge_sort():
    # Test case with an empty list
    arr = []
    merge_sort(arr)
    assert arr == []

    def test_merge_sort():
      # Test case with a single element
      arr = [5]
      merge_sort(arr)
      assert arr == [5]

      # Test case with two elements in sorted order
      arr = [3, 7]
      merge_sort(arr)
      assert arr == [3, 7]


    def test_merge():
      # Test case with two sorted arrays
      left = [1, 3, 5]
      right = [2, 4, 6]
      arr = [0] * (len(left) + len(right))
      merge(left, right, arr)
      assert arr == [1, 2, 3, 4, 5, 6]

