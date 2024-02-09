import time
from supported_algorithms import algorithms

def execute_sorting_algorithm(algorithm_name: str, array: list) -> dict:
    algorithm_func = algorithms.get(algorithm_name.lower())
    if algorithm_func is None:
        return None

    start_time = time.time()
    sorted_array = algorithm_func(array)
    time_taken = time.time() - start_time
    time_taken_ms = round(time_taken * 1000, 3)

    return {
        "name": algorithm_name.replace("_", " ").title(),
        "timeTaken": time_taken_ms,
        "sortedArray": sorted_array
    }
