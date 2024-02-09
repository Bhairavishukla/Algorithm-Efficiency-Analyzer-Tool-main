import time
import matplotlib.pyplot as plt
import random

def generate_random_array(size):
    # Generate an array with 'size' random integers
    # The range of integers is from 1 to 100, but you can modify it as needed
    return [random.randint(1, 100) for _ in range(size)]




def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge(leftHalf,rightHalf):
    sorted_list=[]
    i=j=0
    while i < len(leftHalf) and j < len(rightHalf):
        if(leftHalf[i] < rightHalf[j]):
            sorted_list.append(leftHalf[i])
            i += 1
        else:
            sorted_list.append(rightHalf[j])
            j += 1
    
    while i<len(leftHalf):
        sorted_list.append(leftHalf[i])
        i += 1
    
    while j<len(rightHalf):
        sorted_list.append(rightHalf[j])
        j += 1 
    
    return sorted_list

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    leftHalf = mergeSort(arr[:mid])
    rightHalf = mergeSort(arr[mid:])

    return merge(leftHalf,rightHalf)

# Test data
size = 200  # Specify the desired size of the array
random_array = generate_random_array(size)


# Measure execution time for insertionSort
start_time = time.time()
insertionSort(random_array.copy())
insertion_sort_time = time.time() - start_time

# Measure execution time for bubbleSort
start_time = time.time()
bubbleSort(random_array.copy())
bubble_sort_time = time.time() - start_time


start_time = time.time()
mergeSort(random_array.copy())
merge_sort_time = time.time() - start_time

# Plotting the results
algorithms = ['Insertion Sort', 'Bubble Sort', 'Merge Sort']
times = [insertion_sort_time, bubble_sort_time, merge_sort_time]
print(times)

plt.bar(algorithms, times, color=['blue', 'green','yellow'])
plt.xlabel('Sorting Algorithm')
plt.ylabel('Execution Time (seconds)')
plt.title('Sorting Algorithm Execution Time Comparison')
plt.show()
