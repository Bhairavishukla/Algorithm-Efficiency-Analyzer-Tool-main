from fastapi import FastAPI
from pydantic import BaseModel
import matplotlib.pyplot as plt
from typing import List 
from fastapi.middleware.cors import CORSMiddleware
import io
import base64
import time
import random

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class SortInput(BaseModel):
    array: List[int]
    algorithm: str  # "merge", "bubble", "quick"

class SortRequest(BaseModel):
    size: int  # Size of the random array


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

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    leftHalf = merge_sort(arr[:mid])
    rightHalf = merge_sort(arr[mid:])

    return merge(leftHalf,rightHalf)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



@app.post("/sort-data")
async def sort_data(request: SortRequest):
    # Generate a random array
    random_array = [random.randint(0, 100) for _ in range(request.size)]

    # Measure execution time for each sorting algorithm
    algorithms = ['Bubble Sort', 'Merge Sort']
    times = []
    
    for sort_function in [ bubbleSort, mergeSort]:
        start_time = time.time()
        sort_function(random_array.copy())
        sort_time = time.time() - start_time
        times.append(sort_time)

    # Create a plot
    fig, ax = plt.subplots()
    ax.bar(algorithms, times, color=['blue', 'green', 'red'])
    ax.set_xlabel('Sorting Algorithm')
    ax.set_ylabel('Execution Time (seconds)')
    ax.set_title('Sorting Algorithm Execution Time Comparison')

    # Save plot to a BytesIO object and encode to base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    return {"times": times, "image": image_base64}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
