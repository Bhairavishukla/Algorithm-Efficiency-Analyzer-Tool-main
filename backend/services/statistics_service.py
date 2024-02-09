import time
from typing import List
from sorting_algorithms.quick_select import quick_select

def calculate_median(array: List[int]) -> float:
    n = len(array)
    if n == 0:
        raise ValueError("Array is empty.")
    sorted_array = sorted(array)
    if n % 2 == 1:
        return float(sorted_array[n // 2])
    else:
        return (sorted_array[n // 2 - 1] + sorted_array[n // 2]) / 2

def find_kth_smallest_element(array: List[int], k: int):
    if k < 1 or k > len(array):
        raise ValueError("k is out of range")
    
    start_time = time.time()
    kth_element = quick_select(array, 0, len(array) - 1, k - 1)
    time_taken = time.time() - start_time
    time_taken_ms = round(time_taken * 1000, 3)

    return {
        "name" : "Quick Select",
        "timeTaken": time_taken_ms,
        "kth_smallest_element": kth_element
    }