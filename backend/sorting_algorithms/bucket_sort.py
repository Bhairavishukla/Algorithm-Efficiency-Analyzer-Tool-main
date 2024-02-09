def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    min_value = min(arr)
    max_value = max(arr)
    bucket_count = 10
    buckets = [[] for _ in range(bucket_count)]
    bucket_range = (max_value - min_value) / bucket_count + 1
    for i in arr:
        index = int((i - min_value) / bucket_range)
        buckets[index].append(i)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr += sorted(bucket)

    return sorted_arr